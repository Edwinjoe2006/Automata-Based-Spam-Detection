"""
Classification Engine: Rule-Based Automata + Optional ML Benchmark
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.preprocessing import normalize_text
from src.regex_patterns import match_experiment_patterns, EXPERIMENTS
from src.automata_engine import AutomataEngine


def classify_rule_based(email_text: str, custom_threshold: int = None) -> dict:
    """
    Evaluates an email using transparent, deterministic automata rules and pattern weights.
    Independent of any machine learning model.
    """
    threshold = custom_threshold if custom_threshold is not None else config.SPAM_SCORE_THRESHOLD
    normalized = normalize_text(email_text)

    if not normalized:
        return {
            "input_text": email_text,
            "normalized_text": "",
            "spam_score": 0,
            "threshold": threshold,
            "is_spam": False,
            "verdict": "HAM",
            "confidence": "100%",
            "triggered_rules": [],
            "matched_keywords": [],
            "integrated_automaton": {
                "initial_state": "Q_INIT",
                "terminal_state": "Q_HAM",
                "trace": [{"step": 0, "state": "Q_INIT", "event": "Empty input string -> default HAM"}]
            },
            "explanation": "Input email is empty or whitespace only. Defaulted to clean HAM."
        }

    match_info = match_experiment_patterns(normalized)
    triggered = match_info["triggered_experiments"]
    matched_keywords = match_info["matched_keywords"]
    flags = match_info["flags"]

    # Calculate weighted risk score
    total_score = 0
    rule_breakdown = []
    for exp in triggered:
        weight = config.PATTERN_WEIGHTS.get(exp["key"], 10)
        total_score += weight
        rule_breakdown.append({
            "id": exp["id"],
            "name": exp["name"],
            "regex": exp["regex"],
            "weight": weight
        })

    is_spam = total_score >= threshold
    verdict = "SPAM" if is_spam else "HAM"

    # Run Integrated Automaton simulation
    integrated_auto = AutomataEngine.simulate_integrated_automaton(flags)

    # Human-readable linguistic explanation
    if is_spam:
        explanation = (
            f"SPAM DETECTED: Risk score {total_score} exceeds threshold of {threshold}. "
            f"Triggered {len(triggered)} suspicious pattern(s): "
            f"{', '.join([r['id'] for r in rule_breakdown])}. "
            f"Integrated Automaton reached terminal state '{integrated_auto['terminal_state']}'."
        )
    else:
        if total_score > 0:
            explanation = (
                f"HAM (CLEAN): Risk score {total_score} is below spam threshold of {threshold}. "
                f"Isolated pattern(s) detected ({', '.join([r['id'] for r in rule_breakdown])}) "
                f"but insufficient to warrant spam classification."
            )
        else:
            explanation = (
                f"HAM (CLEAN): Zero suspicious automata patterns triggered. "
                f"Automaton halted in safe state '{integrated_auto['terminal_state']}'."
            )

    return {
        "input_text": email_text,
        "normalized_text": normalized,
        "spam_score": total_score,
        "threshold": threshold,
        "is_spam": is_spam,
        "verdict": verdict,
        "confidence": f"{min(100, int((total_score / max(threshold, 1)) * 50) if not is_spam else 50 + int((total_score / 150) * 50))}%",
        "triggered_rules": rule_breakdown,
        "matched_keywords": matched_keywords,
        "integrated_automaton": integrated_auto,
        "explanation": explanation
    }


class MLClassifier:
    """
    Optional Machine Learning Baseline (TF-IDF + Logistic Regression).
    Clearly demarcated from the primary Formal Languages & Automata system.
    """
    _instance = None

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=config.ML_MAX_FEATURES,
            stop_words="english",
            ngram_range=(1, 2)
        )
        self.model = LogisticRegression(
            max_iter=500,
            random_state=config.ML_RANDOM_STATE
        )
        self.is_trained = False
        self.metrics = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MLClassifier()
        return cls._instance

    def train_and_evaluate(self, df: pd.DataFrame) -> dict:
        """
        Trains TF-IDF + LogisticRegression on 80% train set, evaluates on 20% held-out test set.
        """
        if len(df) < 20:
            return {"trained": False, "error": "Insufficient records to train ML model."}

        X = df["text"].values
        y = df["label"].values

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=config.ML_TEST_SIZE,
            random_state=config.ML_RANDOM_STATE,
            stratify=y
        )

        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        self.model.fit(X_train_vec, y_train)
        self.is_trained = True

        y_pred = self.model.predict(X_test_vec)
        cm = confusion_matrix(y_test, y_pred)

        self.metrics = {
            "trained": True,
            "train_samples": len(X_train),
            "test_samples": len(X_test),
            "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
            "precision": round(float(precision_score(y_test, y_pred, zero_division=0)), 4),
            "recall": round(float(recall_score(y_test, y_pred, zero_division=0)), 4),
            "f1_score": round(float(f1_score(y_test, y_pred, zero_division=0)), 4),
            "confusion_matrix": {
                "tn": int(cm[0][0]),
                "fp": int(cm[0][1]),
                "fn": int(cm[1][0]),
                "tp": int(cm[1][1])
            }
        }
        return self.metrics

    def predict(self, text: str) -> dict:
        """
        Predicts spam probability using trained ML model.
        """
        if not self.is_trained:
            return {"error": "ML model not trained yet."}

        norm_text = normalize_text(text)
        vec = self.vectorizer.transform([norm_text])
        pred = int(self.model.predict(vec)[0])
        prob = self.model.predict_proba(vec)[0]

        return {
            "ml_prediction": "SPAM" if pred == 1 else "HAM",
            "ml_label": pred,
            "spam_probability": round(float(prob[1]) * 100, 2),
            "ham_probability": round(float(prob[0]) * 100, 2)
        }
