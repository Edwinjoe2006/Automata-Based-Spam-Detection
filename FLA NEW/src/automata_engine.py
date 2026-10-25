"""
Automata Simulation Engine
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import xml.etree.ElementTree as ET
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.regex_patterns import EXPERIMENTS


class AutomataEngine:
    """
    Simulates Deterministic and Non-deterministic Finite Automata for Spam Pattern Detection.
    """

    @staticmethod
    def simulate_dfa(states: list, initial_state: str, accepting_states: list,
                     transitions: list, input_string: str) -> dict:
        """
        Generic DFA simulator.
        transitions format: list of (from_state, symbol, to_state)
        """
        current_state = initial_state
        trace = []
        is_accepted = False

        # Build lookup table: {state: {symbol: next_state}}
        trans_map = {}
        for (u, sym, v) in transitions:
            if u not in trans_map:
                trans_map[u] = {}
            trans_map[u][sym] = v

        for i, char in enumerate(input_string):
            next_state = None
            if current_state in trans_map:
                if char in trans_map[current_state]:
                    next_state = trans_map[current_state][char]
                elif "any" in trans_map[current_state]:
                    next_state = trans_map[current_state]["any"]
                elif "other" in trans_map[current_state]:
                    next_state = trans_map[current_state]["other"]

            if next_state:
                trace.append({
                    "step": i + 1,
                    "from_state": current_state,
                    "symbol": char,
                    "to_state": next_state
                })
                current_state = next_state
            else:
                # Dead state or undefined transition
                break

        is_accepted = current_state in accepting_states

        return {
            "initial_state": initial_state,
            "final_state": current_state,
            "is_accepted": is_accepted,
            "trace": trace
        }

    @staticmethod
    def simulate_integrated_automaton(triggered_flags: dict) -> dict:
        """
        Simulates Experiment 10: Integrated Spam Decision Automaton.
        States: Q_INIT -> Q_SUSP -> Q_HIGH -> Q_SPAM / Q_HAM
        """
        state = "Q_INIT"
        trace = [{"step": 0, "state": state, "event": "Start"}]

        has_phish = triggered_flags.get("EXP07_ACCOUNT_VERIFY", False) or triggered_flags.get("EXP05_SUSPICIOUS_URL", False)
        has_promo = triggered_flags.get("EXP01_FREE", False) or triggered_flags.get("EXP02_WIN_PRIZE", False) or triggered_flags.get("EXP06_MONEY_REWARD", False)
        has_urgency = triggered_flags.get("EXP03_URGENT", False) or triggered_flags.get("EXP04_CLICK_HERE", False) or triggered_flags.get("EXP08_EXCLAMATIONS", False)

        step = 1
        if has_phish and (has_promo or has_urgency):
            state = "Q_HIGH"
            trace.append({"step": step, "state": state, "event": "High Risk Phishing & Urgency detected"})
            step += 1
            state = "Q_SPAM"
            trace.append({"step": step, "state": state, "event": "Accepting State Reached -> SPAM"})
        elif has_promo and has_urgency:
            state = "Q_SUSP"
            trace.append({"step": step, "state": state, "event": "Promotional Lure + Urgency Pressure"})
            step += 1
            state = "Q_SPAM"
            trace.append({"step": step, "state": state, "event": "Cumulative Threshold Met -> SPAM"})
        elif has_phish:
            state = "Q_HIGH"
            trace.append({"step": step, "state": state, "event": "Phishing Credential Alert Detected"})
            step += 1
            state = "Q_SPAM"
            trace.append({"step": step, "state": state, "event": "High Security Threat -> SPAM"})
        elif has_promo or has_urgency:
            state = "Q_SUSP"
            trace.append({"step": step, "state": state, "event": "Isolated Keyword Suspicion"})
            step += 1
            state = "Q_HAM"
            trace.append({"step": step, "state": state, "event": "Insufficient Evidence -> HAM"})
        else:
            state = "Q_HAM"
            trace.append({"step": step, "state": state, "event": "No Malicious Patterns -> Clean HAM"})

        return {
            "initial_state": "Q_INIT",
            "terminal_state": state,
            "is_spam": state == "Q_SPAM",
            "trace": trace
        }

    @staticmethod
    def validate_jff_files() -> dict:
        """
        Validates all 10 JFLAP .jff files in the automata directory.
        """
        results = {}
        for exp in EXPERIMENTS:
            filename = exp["jff_file"]
            path = os.path.join(config.AUTOMATA_DIR, filename)
            if not os.path.exists(path):
                results[filename] = {"exists": False, "valid_xml": False, "error": "File not found"}
                continue
            try:
                tree = ET.parse(path)
                root = tree.getroot()
                is_fa = root.find("type") is not None and root.find("type").text == "fa"
                state_count = len(root.findall(".//state"))
                trans_count = len(root.findall(".//transition"))
                results[filename] = {
                    "exists": True,
                    "valid_xml": True,
                    "is_fa": is_fa,
                    "state_count": state_count,
                    "transition_count": trans_count
                }
            except Exception as e:
                results[filename] = {"exists": True, "valid_xml": False, "error": str(e)}

        return results
