"""
Formal Languages and Automata (FLA) Academic Project
10 Standard Test Cases: 5 Spam, 5 Ham
"""

import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.automata import classify_email

TEST_CASES = [
    # -------------------------------------------------------------
    # 5 SPAM TEST CASES
    # -------------------------------------------------------------
    {
        "category": "SPAM",
        "id": 1,
        "input": "Congratulations! You won a free prize."
    },
    {
        "category": "SPAM",
        "id": 2,
        "input": "Claim your bonus money now."
    },
    {
        "category": "SPAM",
        "id": 3,
        "input": "Click here to receive your reward."
    },
    {
        "category": "SPAM",
        "id": 4,
        "input": "Urgent offer! You are a winner."
    },
    {
        "category": "SPAM",
        "id": 5,
        "input": "You have won a cash prize. Claim now."
    },

    # -------------------------------------------------------------
    # 5 HAM TEST CASES
    # -------------------------------------------------------------
    {
        "category": "HAM",
        "id": 6,
        "input": "The meeting is scheduled for tomorrow."
    },
    {
        "category": "HAM",
        "id": 7,
        "input": "Please send me the project report."
    },
    {
        "category": "HAM",
        "id": 8,
        "input": "Your class starts at 10 AM."
    },
    {
        "category": "HAM",
        "id": 9,
        "input": "Can you share the assignment notes?"
    },
    {
        "category": "HAM",
        "id": 10,
        "input": "The department meeting has been postponed."
    }
]


def run_all_tests():
    print("=" * 80)
    print("  FLA PROJECT: AUTOMATA-BASED SPAM EMAIL DETECTION TEST SUITE (10 CASES)")
    print("=" * 80)

    for tc in TEST_CASES:
        res = classify_email(tc["input"])
        print(f"\nTest Case #{tc['id']} [{tc['category']} Target]")
        print("-" * 50)
        print(f"Input              : {res['email_text']}")
        kw_str = ", ".join(res['detected_keywords']) if res['detected_keywords'] else "None"
        print(f"Detected keywords  : {kw_str}")
        print(f"Symbolic string    : {res['symbolic_string']}")
        print(f"DFA result         : {res['dfa_result']}")
        print(f"Classification     : {res['final_classification']}")
        print(f"Reason             : {res['reason']}")

    print("\n" + "=" * 80)
    print("  All 10 test cases executed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    run_all_tests()
