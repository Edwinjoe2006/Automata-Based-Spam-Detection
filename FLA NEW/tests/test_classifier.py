"""
Comprehensive Test Suite (20+ Documented Test Cases)
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import pytest
import sys
import os
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.classifier import classify_rule_based
from src.preprocessing import validate_uploaded_csv

# -------------------------------------------------------------
# 20+ DOCUMENTED TEST CASES
# -------------------------------------------------------------
TEST_SUITE_CASES = [
    # 1-5: Clearly Legitimate Emails (Target: HAM)
    {"id": "TC01", "type": "HAM", "text": "The department project review meeting is scheduled for tomorrow at 10 AM.", "expected": "HAM"},
    {"id": "TC02", "type": "HAM", "text": "Please find attached the lab assignment report for Formal Languages and Automata.", "expected": "HAM"},
    {"id": "TC03", "type": "HAM", "text": "Can you share the lecture slides from yesterday's compiler design seminar?", "expected": "HAM"},
    {"id": "TC04", "type": "HAM", "text": "Your library book loan period expires on Monday. Please renew online if needed.", "expected": "HAM"},
    {"id": "TC05", "type": "HAM", "text": "Faculty advising hours will be held between 2 PM and 4 PM in cabin 204.", "expected": "HAM"},

    # 6-10: Obvious Spam Emails (Target: SPAM)
    {"id": "TC06", "type": "SPAM", "text": "Congratulations! You won a free prize. Click here to claim your cash bonus of $5000 now!", "expected": "SPAM"},
    {"id": "TC07", "type": "SPAM", "text": "Urgent offer! You are selected as our winner. Claim your bonus money immediately.", "expected": "SPAM"},
    {"id": "TC08", "type": "SPAM", "text": "Claim $1000 dollars free cash reward today! Click below to collect jackpot.", "expected": "SPAM"},
    {"id": "TC09", "type": "SPAM", "text": "Final warning: Claim your winning prize payout before offer expires today!!", "expected": "SPAM"},
    {"id": "TC10", "type": "SPAM", "text": "Act now! Free complimentary entry into our million dollar cash prize draw.", "expected": "SPAM"},

    # 11-12: Suspicious URLs & Phishing
    {"id": "TC11", "type": "SPAM", "text": "URGENT SECURITY ALERT: Verify your account password immediately at http://192.168.1.1/login", "expected": "SPAM"},
    {"id": "TC12", "type": "SPAM", "text": "Your account is compromised! Click link at http://phishing-site.xyz/update to verify account.", "expected": "SPAM"},

    # 13-14: Mixed Legitimate & Suspicious Keywords (Edge Cases)
    {"id": "TC13", "type": "HAM_EDGE", "text": "We have a free slot available in the computer lab if students wish to practice JFLAP.", "expected": "HAM"},
    {"id": "TC14", "type": "HAM_EDGE", "text": "Please verify your attendance for tomorrow's departmental project presentation.", "expected": "HAM"},

    # 15-16: Empty and Whitespace Messages
    {"id": "TC15", "type": "EMPTY", "text": "", "expected": "HAM"},
    {"id": "TC16", "type": "WHITESPACE", "text": "   \n\t   ", "expected": "HAM"},

    # 17-18: Non-Standard Capitalization & Punctuation Abuse
    {"id": "TC17", "type": "CAPS_SPAM", "text": "fReE pRiZe WiNnEr! cLiCk hErE tO cLaIm $5000 nOw!", "expected": "SPAM"},
    {"id": "TC18", "type": "PUNCT_SPAM", "text": "CLAIM YOUR CASH NOW!!!! HURRY UP, WINNER$$$$ FREE BONUS!!", "expected": "SPAM"},

    # 19-20: Multi-Rule Synergies & Boundary Phishing
    {"id": "TC19", "type": "MULTI_RULE", "text": "Urgent! Reset password now or account suspension will occur. Click here.", "expected": "SPAM"},
    {"id": "TC20", "type": "MULTI_RULE", "text": "Special complimentary bonus cash reward offered exclusively for you. Act now!", "expected": "SPAM"}
]


@pytest.mark.parametrize("case", TEST_SUITE_CASES)
def test_classifier_cases(case):
    """
    Executes all 20 documented test cases against the Rule-Based Automata engine.
    """
    res = classify_rule_based(case["text"])
    assert res["verdict"] == case["expected"], (
        f"Failed {case['id']} ({case['type']}): Input '{case['text']}' "
        f"yielded {res['verdict']} with score {res['spam_score']} (Expected {case['expected']})"
    )


def test_schema_validation_unexpected_columns(tmp_path):
    """
    Tests handling of unexpected column names in uploaded CSV files.
    """
    csv_file = tmp_path / "custom_test.csv"
    df = pd.DataFrame({
        "random_id": [1, 2],
        "content_body": ["Hello friend", "Claim free prize $5000 now!"],
        "target_class": ["ham", "spam"]
    })
    df.to_csv(csv_file, index=False)

    report = validate_uploaded_csv(str(csv_file))
    assert report["valid"] is True
    assert report["total_rows"] == 2
    assert report["missing_text_count"] == 0
