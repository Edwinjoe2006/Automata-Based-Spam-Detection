"""
Configuration Module for Automata-Based Spam Email Detection
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATASET_PATH = os.path.join(DATA_DIR, "dataset.csv")
AUTOMATA_DIR = os.path.join(BASE_DIR, "automata")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# Kaggle Dataset Source Citation
DATASET_KAGGLE_URL = "https://www.kaggle.com/datasets/ssssws/spam-email-detection-dataset-clean-and-ml-ready"
DATASET_KAGGLE_AUTHOR = "Thanh Nhan Nguyen (ssssws)"
DATASET_ORIGINAL_FILENAME = "spam_email_dataset.csv"

# Dynamic Column Detection Candidates
TEXT_COLUMN_CANDIDATES = [
    "email_text", "text", "body", "content", "email", "message", "subject_body"
]
LABEL_COLUMN_CANDIDATES = [
    "label", "spam", "class", "target", "category", "is_spam"
]

# Label Normalization Map to binary: 1 = Spam, 0 = Ham
LABEL_NORMALIZATION = {
    "1": 1, 1: 1, "spam": 1, "Spam": 1, "SPAM": 1, "malicious": 1,
    "0": 0, 0: 0, "ham": 0, "Ham": 0, "HAM": 0, "legitimate": 0, "non-spam": 0
}

# Rule-Based Spam Scoring Weights (Threshold = 40)
SPAM_SCORE_THRESHOLD = 40

PATTERN_WEIGHTS = {
    "EXP01_FREE": 20,              # Promotional incentive
    "EXP02_WIN_PRIZE": 25,         # Lottery / Prize lure
    "EXP03_URGENT": 20,            # High-pressure urgency
    "EXP04_CLICK_HERE": 20,        # Call to action directive
    "EXP05_SUSPICIOUS_URL": 25,    # Raw IP or suspicious hyperlinking
    "EXP06_MONEY_REWARD": 20,      # Financial terms / Cash offers
    "EXP07_ACCOUNT_VERIFY": 30,    # Credential harvesting / Phishing
    "EXP08_EXCLAMATIONS": 15,      # Artificial excitement / Punctuation abuse
    "EXP09_MULTI_PATTERN": 15,     # Synergy bonus when >= 2 categories match
}

# Machine Learning Parameters (TF-IDF + Logistic Regression)
ML_TEST_SIZE = 0.20
ML_RANDOM_STATE = 42
ML_MAX_FEATURES = 2500

# Built-in Demo Data (Used if dataset.csv is missing or corrupt)
DEMO_DATA = [
    {"text": "Congratulations! You won a free prize. Click here to claim your cash bonus.", "label": 1},
    {"text": "URGENT SECURITY ALERT: Verify your account password immediately at http://192.168.1.1/login", "label": 1},
    {"text": "Exclusive offer! Claim $5000 dollars today now!!!! Click here.", "label": 1},
    {"text": "You have been selected as our lottery winner. Act now to receive your reward.", "label": 1},
    {"text": "Final notice: urgent account suspension pending. Click link to update account.", "label": 1},
    {"text": "The project review meeting is scheduled for tomorrow at 10 AM in Lab 3.", "label": 0},
    {"text": "Please find attached the department seminar report for Formal Language and Automata.", "label": 0},
    {"text": "Can you share the lecture notes and assignment 2 problem statements before Friday?", "label": 0},
    {"text": "Your library book is due for return on Monday. Please renew if needed.", "label": 0},
    {"text": "The class on compiler design will be held online via the university portal.", "label": 0}
]
