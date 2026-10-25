"""
Evaluation and Comparison Module
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.preprocessing import load_dataset
from src.classifier import classify_rule_based, MLClassifier


def evaluate_both_models(df: pd.DataFrame = None) -> dict:
    """
    Evaluates both the Rule-Based Automata system and the ML baseline
    on the exact same held-out test set (20% of dataset).
    """
    if df is None:
        df, _ = load_dataset()

    X = df["text"].values
    y = df["label"].values

    if len(df) < 10:
        return {"error": "Dataset too small for formal evaluation."}

    # Consistent split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config.ML_TEST_SIZE,
        random_state=config.ML_RANDOM_STATE,
        stratify=y
    )

    # 1. Evaluate Rule-Based Automata Classifier on X_test
    rule_preds = []
    for text in X_test:
        res = classify_rule_based(text)
        rule_preds.append(1 if res["is_spam"] else 0)

    cm_rule = confusion_matrix(y_test, rule_preds)
    rule_metrics = {
        "model_name": "Rule-Based Automata Engine",
        "paradigm": "Formal Languages, Regex & Finite Automata",
        "test_samples": len(X_test),
        "accuracy": round(float(accuracy_score(y_test, rule_preds)), 4),
        "precision": round(float(precision_score(y_test, rule_preds, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, rule_preds, zero_division=0)), 4),
        "f1_score": round(float(f1_score(y_test, rule_preds, zero_division=0)), 4),
        "confusion_matrix": {
            "tn": int(cm_rule[0][0]),
            "fp": int(cm_rule[0][1]),
            "fn": int(cm_rule[1][0]),
            "tp": int(cm_rule[1][1])
        }
    }

    # 2. Train and Evaluate ML Classifier on the exact same split
    ml = MLClassifier.get_instance()
    ml_metrics_raw = ml.train_and_evaluate(df)

    ml_metrics = {
        "model_name": "Machine Learning Baseline",
        "paradigm": "TF-IDF + Logistic Regression",
        "test_samples": ml_metrics_raw.get("test_samples", len(X_test)),
        "accuracy": ml_metrics_raw.get("accuracy", 0.0),
        "precision": ml_metrics_raw.get("precision", 0.0),
        "recall": ml_metrics_raw.get("recall", 0.0),
        "f1_score": ml_metrics_raw.get("f1_score", 0.0),
        "confusion_matrix": ml_metrics_raw.get("confusion_matrix", {"tn": 0, "fp": 0, "fn": 0, "tp": 0})
    }

    comparison = {
        "test_set_size": len(X_test),
        "rule_based": rule_metrics,
        "machine_learning": ml_metrics,
        "discussion": {
            "rule_based_strengths": "100% transparent, deterministic, zero training overhead, exact mathematical state proofs.",
            "rule_based_limitations": "Susceptible to false negatives if spammers obfuscate keywords or invent novel templates.",
            "ml_strengths": "Learns statistical feature weights from corpus distributions, capturing latent vocabulary.",
            "ml_limitations": "Black box, requires substantial training data, can overfit dataset-specific artifacts."
        }
    }

    return comparison


if __name__ == "__main__":
    print("Evaluating models on dataset...")
    results = evaluate_both_models()
    print("Rule-Based Accuracy:", results["rule_based"]["accuracy"])
    print("ML Baseline Accuracy:", results["machine_learning"]["accuracy"])
