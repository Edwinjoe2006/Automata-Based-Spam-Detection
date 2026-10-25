"""
Flask Web Application: Automata-Based Email Spam Detection and Classification
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import sys
from flask import Flask, render_template, request, jsonify, send_from_directory

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import config
from src.preprocessing import load_dataset, validate_uploaded_csv
from src.regex_patterns import EXPERIMENTS
from src.classifier import classify_rule_based, MLClassifier
from src.evaluation import evaluate_both_models

app = Flask(__name__)
app.config["SECRET_KEY"] = "academic-fla-spam-project-secret-key"

# Pre-load dataset and initial evaluation metrics on startup
DATASET_DF, DATASET_STATS = load_dataset()
CACHED_METRICS = evaluate_both_models(DATASET_DF)


@app.route("/")
def dashboard():
    """Page 1: System Dashboard with dataset statistics and model metrics"""
    return render_template(
        "index.html",
        active_page="dashboard",
        stats=DATASET_STATS,
        metrics=CACHED_METRICS,
        experiments=EXPERIMENTS
    )


@app.route("/analyze", methods=["GET", "POST"])
def analyze_page():
    """Page 2: Interactive Email Analyzer with rule breakdown and state traces"""
    email_text = ""
    threshold = config.SPAM_SCORE_THRESHOLD
    result = None
    ml_result = None

    if request.method == "POST":
        email_text = request.form.get("email_text", "").strip()
        custom_th = request.form.get("threshold", "").strip()
        if custom_th.isdigit():
            threshold = int(custom_th)

        if email_text:
            result = classify_rule_based(email_text, custom_threshold=threshold)
            ml = MLClassifier.get_instance()
            if ml.is_trained:
                ml_result = ml.predict(email_text)

    return render_template(
        "analyze.html",
        active_page="analyze",
        email_text=email_text,
        threshold=threshold,
        result=result,
        ml_result=ml_result
    )


@app.route("/explorer", methods=["GET", "POST"])
def explorer_page():
    """Page 3: Dataset Explorer with schema validation and CSV upload"""
    upload_report = None

    if request.method == "POST":
        uploaded_file = request.files.get("csv_file")
        if uploaded_file and uploaded_file.filename.endswith(".csv"):
            temp_path = os.path.join(PROJECT_ROOT, "data", "temp_uploaded.csv")
            uploaded_file.save(temp_path)
            upload_report = validate_uploaded_csv(temp_path)

    preview_rows = DATASET_DF.head(10).to_dict(orient="records")

    return render_template(
        "explorer.html",
        active_page="explorer",
        stats=DATASET_STATS,
        preview_rows=preview_rows,
        upload_report=upload_report
    )


@app.route("/lab")
def lab_page():
    """Page 4: Automata Laboratory showcasing all 10 experiments and transition tables"""
    return render_template(
        "lab.html",
        active_page="lab",
        experiments=EXPERIMENTS
    )


@app.route("/evaluation")
def evaluation_page():
    """Page 5: Model Evaluation and Rule-Based vs ML Comparison"""
    return render_template(
        "evaluation.html",
        active_page="evaluation",
        eval_results=CACHED_METRICS
    )


@app.route("/download/<path:filename>")
def download_jff(filename):
    """Allows downloading of .jff automata files for JFLAP simulation"""
    return send_from_directory(config.AUTOMATA_DIR, filename, as_attachment=True)


@app.route("/api/classify", methods=["POST"])
def api_classify():
    """REST API endpoint for automated testing and programmatic evaluation"""
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    threshold = data.get("threshold", config.SPAM_SCORE_THRESHOLD)

    res = classify_rule_based(text, custom_threshold=threshold)
    return jsonify(res)


if __name__ == "__main__":
    print(f"Launching B.Tech IT FLA Project on http://127.0.0.1:5000 ...")
    app.run(debug=True, host="127.0.0.1", port=5000)
