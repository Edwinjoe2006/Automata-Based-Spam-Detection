"""
Formal Regular Expression Definitions & Automata Experiments
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import re

EXPERIMENTS = [
    {
        "id": "EXP01",
        "key": "EXP01_FREE",
        "name": "Promotional 'FREE' Keyword Recognizer",
        "problem_statement": "Detect unsolicited promotional emails enticing recipients with complimentary or zero-cost lures.",
        "formal_language": "L1 = { w in Sigma* | w contains substring 'FREE' as a discrete token }",
        "alphabet": "Sigma = { F, R, E, other } or token sequence",
        "regex": r"(?i)\b(free|freebie|complimentary)\b",
        "compiled": re.compile(r"\b(free|freebie|complimentary)\b", re.IGNORECASE),
        "jff_file": "experiment_01.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2", "q3", "q4"],
        "initial_state": "q0",
        "accepting_states": ["q4"],
        "transitions": [
            ("q0", "F", "q1"),
            ("q1", "R", "q2"),
            ("q2", "E", "q3"),
            ("q3", "E", "q4"),
            ("q4", "any", "q4")
        ],
        "accepted_test_inputs": ["Claim your free gift today", "Exclusive freebie for members", "Free trial access"],
        "rejected_test_inputs": ["The freeze warning was issued", "Freedom of speech is vital", "Meeting at noon"],
        "explanation": "State q0 expects 'F'. On reading 'R', moves to q2; on first 'E' to q3; on final 'E' reaches accepting state q4.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_01.jff -> Input -> Fast Run -> Type 'FREE' -> Accept."
    },
    {
        "id": "EXP02",
        "key": "EXP02_WIN_PRIZE",
        "name": "Lottery / Contest 'WIN' or 'PRIZE' Recognizer",
        "problem_statement": "Detect deceptive lottery notices informing recipients they have won a contest or prize draw.",
        "formal_language": "L2 = { w in Sigma* | w contains substring 'WIN' or 'PRIZE' }",
        "alphabet": "Sigma = { W, I, N, P, R, Z, E, other }",
        "regex": r"(?i)\b(win|winner|won|winning|prize|reward|jackpot)\b",
        "compiled": re.compile(r"\b(win|winner|won|winning|prize|reward|jackpot)\b", re.IGNORECASE),
        "jff_file": "experiment_02.jff",
        "automata_type": "NFA -> DFA",
        "states": ["q0", "q1", "q2", "q3", "q4", "q5", "q6"],
        "initial_state": "q0",
        "accepting_states": ["q3", "q6"],
        "transitions": [
            ("q0", "W", "q1"), ("q1", "I", "q2"), ("q2", "N", "q3"), ("q3", "any", "q3"),
            ("q0", "P", "q4"), ("q4", "R", "q5"), ("q5", "Z", "q6"), ("q6", "any", "q6")
        ],
        "accepted_test_inputs": ["Congratulations, you won!", "Claim your prize money", "You are the selected winner"],
        "rejected_test_inputs": ["Window is open", "Praise the student for work", "Department seminar scheduled"],
        "explanation": "Branching NFA path: Branch 1 accepts 'W-I-N' reaching q3; Branch 2 accepts 'P-R-I-Z-E' reaching q6.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_02.jff -> Input -> Step with State -> Test 'WIN' and 'PRIZE'."
    },
    {
        "id": "EXP03",
        "key": "EXP03_URGENT",
        "name": "High-Pressure 'URGENT' or 'ACT NOW' Recognizer",
        "problem_statement": "Identify psychological manipulation techniques creating artificial panic and time-sensitive pressure.",
        "formal_language": "L3 = { w in Sigma* | w contains 'URGENT' or 'ACT NOW' or 'EXPIRES' }",
        "alphabet": "Sigma = { U, R, G, E, N, T, A, C, N, O, W, other }",
        "regex": r"(?i)\b(urgent|urgently|act now|expires? today|immediate action|respond immediately)\b",
        "compiled": re.compile(r"\b(urgent|urgently|act now|expires? today|immediate action|respond immediately)\b", re.IGNORECASE),
        "jff_file": "experiment_03.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2", "q3", "q4", "q5", "q6"],
        "initial_state": "q0",
        "accepting_states": ["q6"],
        "transitions": [
            ("q0", "U", "q1"), ("q1", "R", "q2"), ("q2", "G", "q3"),
            ("q3", "E", "q4"), ("q4", "N", "q5"), ("q5", "T", "q6"), ("q6", "any", "q6")
        ],
        "accepted_test_inputs": ["Urgent attention required!", "Act now before offer ends", "Immediate action required"],
        "rejected_test_inputs": ["Our agent will assist you", "Fact sheet provided", "Please submit next week"],
        "explanation": "State transitions sequentially recognize the spelling sequence 'U-R-G-E-N-T' terminating in q6.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_03.jff -> Input -> Fast Run -> Type 'URGENT'."
    },
    {
        "id": "EXP04",
        "key": "EXP04_CLICK_HERE",
        "name": "Call-to-Action 'CLICK HERE' Recognizer",
        "problem_statement": "Detect explicit directives coercing users into clicking potentially harmful hyperlinks.",
        "formal_language": "L4 = { w in Sigma* | w contains 'CLICK HERE' or 'CLICK LINK' }",
        "alphabet": "Sigma = { C, L, I, C, K, H, E, R, E, other }",
        "regex": r"(?i)\b(click here|click link|click below|tap here|click this link)\b",
        "compiled": re.compile(r"\b(click here|click link|click below|tap here|click this link)\b", re.IGNORECASE),
        "jff_file": "experiment_04.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2", "q3", "q4", "q5"],
        "initial_state": "q0",
        "accepting_states": ["q5"],
        "transitions": [
            ("q0", "C", "q1"), ("q1", "L", "q2"), ("q2", "I", "q3"),
            ("q3", "C", "q4"), ("q4", "K", "q5"), ("q5", "any", "q5")
        ],
        "accepted_test_inputs": ["Click here to verify now", "Please click below for details", "Tap here to continue"],
        "rejected_test_inputs": ["The clock is ticking", "Send file by clicking send", "Assignment submission notes"],
        "explanation": "Recognizes the directive keyword 'CLICK' followed by contextual target, reaching accepting state q5.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_04.jff -> Input -> Fast Run -> Type 'CLICK'."
    },
    {
        "id": "EXP05",
        "key": "EXP05_SUSPICIOUS_URL",
        "name": "Suspicious URL and Raw IP Recognizer",
        "problem_statement": "Identify unverified hyperlinks, insecure protocols, or raw IP addresses used in phishing emails.",
        "formal_language": "L5 = { w in Sigma* | w contains http:// or https:// or raw IPv4 pattern }",
        "alphabet": "Sigma = { h, t, p, s, :, /, ., digits, other }",
        "regex": r"(https?://\S+|www\.\S+|\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)",
        "compiled": re.compile(r"(https?://\S+|www\.\S+|\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)", re.IGNORECASE),
        "jff_file": "experiment_05.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"],
        "initial_state": "q0",
        "accepting_states": ["q7"],
        "transitions": [
            ("q0", "h", "q1"), ("q1", "t", "q2"), ("q2", "t", "q3"), ("q3", "p", "q4"),
            ("q4", ":", "q5"), ("q5", "/", "q6"), ("q6", "/", "q7"), ("q7", "any", "q7")
        ],
        "accepted_test_inputs": ["Visit http://192.168.1.1/login", "Go to https://claim-rewards.xyz", "Check www.free-prize.biz"],
        "rejected_test_inputs": ["No links present in this text", "Read chapter 4 section 2", "Meet me at classroom"],
        "explanation": "Validates the prefix 'http://' character by character, moving from q0 through q7 (accepting state).",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_05.jff -> Input -> Fast Run -> Type 'http://'."
    },
    {
        "id": "EXP06",
        "key": "EXP06_MONEY_REWARD",
        "name": "Currency & Financial Bounty Recognizer",
        "problem_statement": "Detect unsolicited monetary promises, currency symbols, or unexpected cash bonuses.",
        "formal_language": "L6 = { w in Sigma* | w contains currency symbol '$' with digits or words 'CASH', 'DOLLARS', 'BONUS' }",
        "alphabet": "Sigma = { $, digits, C, A, S, H, B, O, N, U, S, other }",
        "regex": r"(\$\s*\d+|\b\d+\s*(dollars?|usd|cash|bonus)\b|\b(cash prize|bonus money|wire transfer)\b)",
        "compiled": re.compile(r"(\$\s*\d+|\b\d+\s*(dollars?|usd|cash|bonus)\b|\b(cash prize|bonus money|wire transfer)\b)", re.IGNORECASE),
        "jff_file": "experiment_06.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2"],
        "initial_state": "q0",
        "accepting_states": ["q2"],
        "transitions": [
            ("q0", "$", "q1"), ("q1", "digit", "q2"), ("q2", "digit", "q2"), ("q2", "any", "q2")
        ],
        "accepted_test_inputs": ["You received $5000 in your account", "Claim 1000 dollars bonus", "Cash prize waiting"],
        "rejected_test_inputs": ["The project report is due", "Department budget review meeting", "Lab experiments conducted"],
        "explanation": "State q0 transitions on '$' to q1, and on reading numerical digits transitions to accepting state q2.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_06.jff -> Input -> Fast Run -> Type '$500'."
    },
    {
        "id": "EXP07",
        "key": "EXP07_ACCOUNT_VERIFY",
        "name": "Account Phishing & Verification Recognizer",
        "problem_statement": "Detect social engineering emails asking to verify credentials, reset passwords, or update security details.",
        "formal_language": "L7 = { w in Sigma* | w contains 'VERIFY ACCOUNT' or 'SECURITY ALERT' or 'RESET PASSWORD' }",
        "alphabet": "Sigma = { Security tokens, letters, whitespace }",
        "regex": r"(?i)\b(verify (your )?account|security alert|reset (your )?password|update (your )?account|account suspension|compromised account)\b",
        "compiled": re.compile(r"\b(verify (your )?account|security alert|reset (your )?password|update (your )?account|account suspension|compromised account)\b", re.IGNORECASE),
        "jff_file": "experiment_07.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2", "q3", "q4", "q5", "q6"],
        "initial_state": "q0",
        "accepting_states": ["q6"],
        "transitions": [
            ("q0", "V", "q1"), ("q1", "E", "q2"), ("q2", "R", "q3"),
            ("q3", "I", "q4"), ("q4", "F", "q5"), ("q5", "Y", "q6"), ("q6", "any", "q6")
        ],
        "accepted_test_inputs": ["Security Alert: Please verify your account", "Reset password immediately", "Account suspension notice"],
        "rejected_test_inputs": ["Class syllabus verification done", "Professors reviewed the lab", "Thank you for the notes"],
        "explanation": "Directly flags deceptive verification tokens that signal credential harvesting scams.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_07.jff -> Input -> Fast Run -> Type 'VERIFY'."
    },
    {
        "id": "EXP08",
        "key": "EXP08_EXCLAMATIONS",
        "name": "Repeated Exclamation Mark Abuse Recognizer",
        "problem_statement": "Detect emotional punctuation exaggeration characterized by multiple consecutive exclamation points.",
        "formal_language": "L8 = { w in Sigma* | w contains '!!' or more repeated exclamations }",
        "alphabet": "Sigma = { !, not_! }",
        "regex": r"!{2,}",
        "compiled": re.compile(r"!{2,}"),
        "jff_file": "experiment_08.jff",
        "automata_type": "DFA",
        "states": ["q0", "q1", "q2"],
        "initial_state": "q0",
        "accepting_states": ["q2"],
        "transitions": [
            ("q0", "!", "q1"), ("q0", "other", "q0"),
            ("q1", "!", "q2"), ("q1", "other", "q0"),
            ("q2", "!", "q2"), ("q2", "other", "q2")
        ],
        "accepted_test_inputs": ["Claim now!!", "Winner, hurry up!!!", "Don't miss this opportunity!!!!"],
        "rejected_test_inputs": ["Please find the report attached.", "Welcome to the class!", "Is the seminar today?"],
        "explanation": "State q0 moves to q1 on first '!'. If another '!' immediately follows, moves to accepting state q2.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_08.jff -> Input -> Fast Run -> Type '!!'."
    },
    {
        "id": "EXP09",
        "key": "EXP09_MULTI_PATTERN",
        "name": "Multi-Pattern Synergy Automaton",
        "problem_statement": "Aggregates individual pattern triggers to recognize when an email triggers 2 or more distinct spam categories.",
        "formal_language": "L9 = { w in Gamma* | |w| >= 2, where Gamma is set of pattern trigger tokens }",
        "alphabet": "Gamma = { T1, T2, T3, T4, T5, T6, T7, T8 }",
        "regex": r"(?=(.*(free|bonus|cash|win|prize|reward))){2,}",
        "compiled": None,  # Simulated via automata state counter
        "jff_file": "experiment_09.jff",
        "automata_type": "DFA Counter",
        "states": ["S0", "S1", "S2"],
        "initial_state": "S0",
        "accepting_states": ["S2"],
        "transitions": [
            ("S0", "Trigger", "S1"),
            ("S1", "Trigger", "S2"),
            ("S2", "Trigger", "S2")
        ],
        "accepted_test_inputs": ["Free prize win", "Urgent cash bonus", "Claim free reward now"],
        "rejected_test_inputs": ["Free sample only", "Win one match", "The meeting starts at 10 AM"],
        "explanation": "Begins at S0 (0 triggers). Moves to S1 on first trigger, and reaches accepting state S2 when >= 2 triggers occur.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_09.jff -> Input -> Multiple Run -> Test strings with 1 vs 2 triggers."
    },
    {
        "id": "EXP10",
        "key": "EXP10_INTEGRATED_DECISION",
        "name": "Integrated Spam Decision Automaton",
        "problem_statement": "Combines lexical triggers, punctuation abuse, and credential risks into an integrated decision state machine.",
        "formal_language": "L10 = Set of all emails that transition through preliminary check states to terminal ACCEPT state.",
        "alphabet": "Sigma = { Clean, Promo, Phish, Urgency, Exclam }",
        "regex": r"(Comprehensive Rule-Based Decision System)",
        "compiled": None,
        "jff_file": "experiment_10.jff",
        "automata_type": "Integrated DFA",
        "states": ["Q_INIT", "Q_SUSP", "Q_HIGH", "Q_SPAM", "Q_HAM"],
        "initial_state": "Q_INIT",
        "accepting_states": ["Q_SPAM"],
        "transitions": [
            ("Q_INIT", "Clean", "Q_HAM"),
            ("Q_INIT", "Promo", "Q_SUSP"),
            ("Q_SUSP", "Urgency", "Q_HIGH"),
            ("Q_HIGH", "Phish", "Q_SPAM"),
            ("Q_INIT", "Phish", "Q_HIGH")
        ],
        "accepted_test_inputs": ["Urgent alert! Verify account at http://phish.com and claim free prize!!"],
        "rejected_test_inputs": ["Please review the project schedule before the committee meeting."],
        "explanation": "Transitions through risk states based on cumulative pattern presence, halting in Q_SPAM if threshold met.",
        "jflap_instructions": "1. Open JFLAP -> Open experiment_10.jff -> Input -> Step with State -> Follow transition to Q_SPAM."
    }
]


def match_experiment_patterns(text: str) -> dict:
    """
    Executes regex pattern matching across all experiments on given text.
    Returns:
        dict: {
            "triggered_experiments": list of experiment dicts,
            "matched_keywords": list of matched string snippets,
            "experiment_flags": dict mapping experiment_id to bool
        }
    """
    triggered = []
    matched_words = []
    flags = {}

    for exp in EXPERIMENTS:
        exp_id = exp["id"]
        exp_key = exp["key"]
        compiled = exp.get("compiled")

        is_match = False
        if compiled is not None:
            matches = compiled.findall(text)
            if matches:
                is_match = True
                # Flatten regex match groups if tuples
                for m in matches:
                    if isinstance(m, tuple):
                        word = next((w for w in m if w), "")
                    else:
                        word = m
                    if word and word not in matched_words:
                        matched_words.append(word)
        flags[exp_key] = is_match
        if is_match:
            triggered.append(exp)

    # Multi-pattern check for EXP09
    distinct_triggers = len(triggered)
    flags["EXP09_MULTI_PATTERN"] = distinct_triggers >= 2
    if distinct_triggers >= 2:
        exp09 = next(e for e in EXPERIMENTS if e["id"] == "EXP09")
        if exp09 not in triggered:
            triggered.append(exp09)

    return {
        "triggered_experiments": triggered,
        "matched_keywords": matched_words,
        "flags": flags,
        "trigger_count": len(triggered)
    }
