"""
JFLAP .jff Automata Generator for Experiments 1 to 10
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import xml.etree.ElementTree as ET

AUTOMATA_DIR = os.path.dirname(os.path.abspath(__file__))

def create_jff(filename, states, transitions):
    """
    states: list of dicts: {'id': '0', 'name': 'q0', 'x': 100.0, 'y': 150.0, 'initial': bool, 'final': bool}
    transitions: list of dicts: {'from': '0', 'to': '1', 'read': 'F'}
    """
    root = ET.Element("structure")
    type_el = ET.SubElement(root, "type")
    type_el.text = "fa"
    auto_el = ET.SubElement(root, "automaton")
    auto_el.append(ET.Comment(" The list of states. "))

    for s in states:
        state_el = ET.SubElement(auto_el, "state", id=str(s["id"]), name=s["name"])
        x_el = ET.SubElement(state_el, "x")
        x_el.text = str(s.get("x", 100.0))
        y_el = ET.SubElement(state_el, "y")
        y_el.text = str(s.get("y", 150.0))
        if s.get("initial", False):
            ET.SubElement(state_el, "initial")
        if s.get("final", False):
            ET.SubElement(state_el, "final")

    auto_el.append(ET.Comment(" The list of transitions. "))
    for t in transitions:
        t_el = ET.SubElement(auto_el, "transition")
        from_el = ET.SubElement(t_el, "from")
        from_el.text = str(t["from"])
        to_el = ET.SubElement(t_el, "to")
        to_el.text = str(t["to"])
        read_el = ET.SubElement(t_el, "read")
        read_el.text = str(t.get("read", ""))

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    filepath = os.path.join(AUTOMATA_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created for JFLAP 7.1 FLA Course-->\n')
        tree.write(f, encoding="utf-8", xml_declaration=False)
    print(f"Generated valid JFLAP file: {filename}")

def build_all_10_experiments():
    # -------------------------------------------------------------
    # Exp 01: FREE
    # -------------------------------------------------------------
    states_01 = [
        {"id": 0, "name": "q0", "x": 80.0, "y": 140.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 200.0, "y": 140.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 320.0, "y": 140.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 440.0, "y": 140.0, "initial": False, "final": False},
        {"id": 4, "name": "q4", "x": 560.0, "y": 140.0, "initial": False, "final": True},
    ]
    trans_01 = [
        {"from": 0, "to": 1, "read": "F"},
        {"from": 1, "to": 2, "read": "R"},
        {"from": 2, "to": 3, "read": "E"},
        {"from": 3, "to": 4, "read": "E"},
        {"from": 4, "to": 4, "read": " "},
    ]
    create_jff("experiment_01.jff", states_01, trans_01)

    # -------------------------------------------------------------
    # Exp 02: WIN / PRIZE
    # -------------------------------------------------------------
    states_02 = [
        {"id": 0, "name": "q0", "x": 100.0, "y": 180.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 240.0, "y": 100.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 380.0, "y": 100.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 520.0, "y": 100.0, "initial": False, "final": True},
        {"id": 4, "name": "q4", "x": 240.0, "y": 260.0, "initial": False, "final": False},
        {"id": 5, "name": "q5", "x": 380.0, "y": 260.0, "initial": False, "final": False},
        {"id": 6, "name": "q6", "x": 520.0, "y": 260.0, "initial": False, "final": True},
    ]
    trans_02 = [
        {"from": 0, "to": 1, "read": "W"},
        {"from": 1, "to": 2, "read": "I"},
        {"from": 2, "to": 3, "read": "N"},
        {"from": 0, "to": 4, "read": "P"},
        {"from": 4, "to": 5, "read": "R"},
        {"from": 5, "to": 6, "read": "Z"},
    ]
    create_jff("experiment_02.jff", states_02, trans_02)

    # -------------------------------------------------------------
    # Exp 03: URGENT / ACT NOW
    # -------------------------------------------------------------
    states_03 = [
        {"id": 0, "name": "q0", "x": 60.0, "y": 140.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 160.0, "y": 140.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 260.0, "y": 140.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 360.0, "y": 140.0, "initial": False, "final": False},
        {"id": 4, "name": "q4", "x": 460.0, "y": 140.0, "initial": False, "final": False},
        {"id": 5, "name": "q5", "x": 560.0, "y": 140.0, "initial": False, "final": False},
        {"id": 6, "name": "q6", "x": 660.0, "y": 140.0, "initial": False, "final": True},
    ]
    trans_03 = [
        {"from": 0, "to": 1, "read": "U"},
        {"from": 1, "to": 2, "read": "R"},
        {"from": 2, "to": 3, "read": "G"},
        {"from": 3, "to": 4, "read": "E"},
        {"from": 4, "to": 5, "read": "N"},
        {"from": 5, "to": 6, "read": "T"},
    ]
    create_jff("experiment_03.jff", states_03, trans_03)

    # -------------------------------------------------------------
    # Exp 04: CLICK HERE
    # -------------------------------------------------------------
    states_04 = [
        {"id": 0, "name": "q0", "x": 80.0, "y": 140.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 200.0, "y": 140.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 320.0, "y": 140.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 440.0, "y": 140.0, "initial": False, "final": False},
        {"id": 4, "name": "q4", "x": 560.0, "y": 140.0, "initial": False, "final": False},
        {"id": 5, "name": "q5", "x": 680.0, "y": 140.0, "initial": False, "final": True},
    ]
    trans_04 = [
        {"from": 0, "to": 1, "read": "C"},
        {"from": 1, "to": 2, "read": "L"},
        {"from": 2, "to": 3, "read": "I"},
        {"from": 3, "to": 4, "read": "C"},
        {"from": 4, "to": 5, "read": "K"},
    ]
    create_jff("experiment_04.jff", states_04, trans_04)

    # -------------------------------------------------------------
    # Exp 05: Suspicious URL
    # -------------------------------------------------------------
    states_05 = [
        {"id": 0, "name": "q0", "x": 60.0, "y": 140.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 150.0, "y": 140.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 240.0, "y": 140.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 330.0, "y": 140.0, "initial": False, "final": False},
        {"id": 4, "name": "q4", "x": 420.0, "y": 140.0, "initial": False, "final": False},
        {"id": 5, "name": "q5", "x": 510.0, "y": 140.0, "initial": False, "final": False},
        {"id": 6, "name": "q6", "x": 600.0, "y": 140.0, "initial": False, "final": False},
        {"id": 7, "name": "q7", "x": 690.0, "y": 140.0, "initial": False, "final": True},
    ]
    trans_05 = [
        {"from": 0, "to": 1, "read": "h"},
        {"from": 1, "to": 2, "read": "t"},
        {"from": 2, "to": 3, "read": "t"},
        {"from": 3, "to": 4, "read": "p"},
        {"from": 4, "to": 5, "read": ":"},
        {"from": 5, "to": 6, "read": "/"},
        {"from": 6, "to": 7, "read": "/"},
        {"from": 7, "to": 7, "read": "w"},
    ]
    create_jff("experiment_05.jff", states_05, trans_05)

    # -------------------------------------------------------------
    # Exp 06: Money / Currency ($)
    # -------------------------------------------------------------
    states_06 = [
        {"id": 0, "name": "q0", "x": 120.0, "y": 150.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 280.0, "y": 150.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 440.0, "y": 150.0, "initial": False, "final": True},
    ]
    trans_06 = [
        {"from": 0, "to": 1, "read": "$"},
        {"from": 1, "to": 2, "read": "1"},
        {"from": 1, "to": 2, "read": "5"},
        {"from": 2, "to": 2, "read": "0"},
    ]
    create_jff("experiment_06.jff", states_06, trans_06)

    # -------------------------------------------------------------
    # Exp 07: Password / Account Verification
    # -------------------------------------------------------------
    states_07 = [
        {"id": 0, "name": "q0", "x": 80.0, "y": 140.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 180.0, "y": 140.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 280.0, "y": 140.0, "initial": False, "final": False},
        {"id": 3, "name": "q3", "x": 380.0, "y": 140.0, "initial": False, "final": False},
        {"id": 4, "name": "q4", "x": 480.0, "y": 140.0, "initial": False, "final": False},
        {"id": 5, "name": "q5", "x": 580.0, "y": 140.0, "initial": False, "final": False},
        {"id": 6, "name": "q6", "x": 680.0, "y": 140.0, "initial": False, "final": True},
    ]
    trans_07 = [
        {"from": 0, "to": 1, "read": "V"},
        {"from": 1, "to": 2, "read": "E"},
        {"from": 2, "to": 3, "read": "R"},
        {"from": 3, "to": 4, "read": "I"},
        {"from": 4, "to": 5, "read": "F"},
        {"from": 5, "to": 6, "read": "Y"},
    ]
    create_jff("experiment_07.jff", states_07, trans_07)

    # -------------------------------------------------------------
    # Exp 08: Repeated Exclamation Marks (!{2,})
    # -------------------------------------------------------------
    states_08 = [
        {"id": 0, "name": "q0", "x": 120.0, "y": 150.0, "initial": True, "final": False},
        {"id": 1, "name": "q1", "x": 280.0, "y": 150.0, "initial": False, "final": False},
        {"id": 2, "name": "q2", "x": 440.0, "y": 150.0, "initial": False, "final": True},
    ]
    trans_08 = [
        {"from": 0, "to": 1, "read": "!"},
        {"from": 1, "to": 2, "read": "!"},
        {"from": 2, "to": 2, "read": "!"},
    ]
    create_jff("experiment_08.jff", states_08, trans_08)

    # -------------------------------------------------------------
    # Exp 09: Multi-Pattern Synergy Counter
    # -------------------------------------------------------------
    states_09 = [
        {"id": 0, "name": "S0", "x": 120.0, "y": 150.0, "initial": True, "final": False},
        {"id": 1, "name": "S1", "x": 280.0, "y": 150.0, "initial": False, "final": False},
        {"id": 2, "name": "S2", "x": 440.0, "y": 150.0, "initial": False, "final": True},
    ]
    trans_09 = [
        {"from": 0, "to": 1, "read": "T"},
        {"from": 1, "to": 2, "read": "T"},
        {"from": 2, "to": 2, "read": "T"},
    ]
    create_jff("experiment_09.jff", states_09, trans_09)

    # -------------------------------------------------------------
    # Exp 10: Integrated Spam Decision Automaton
    # -------------------------------------------------------------
    states_10 = [
        {"id": 0, "name": "Q_INIT", "x": 80.0, "y": 180.0, "initial": True, "final": False},
        {"id": 1, "name": "Q_SUSP", "x": 260.0, "y": 100.0, "initial": False, "final": False},
        {"id": 2, "name": "Q_HIGH", "x": 440.0, "y": 100.0, "initial": False, "final": False},
        {"id": 3, "name": "Q_SPAM", "x": 620.0, "y": 180.0, "initial": False, "final": True},
        {"id": 4, "name": "Q_HAM", "x": 350.0, "y": 280.0, "initial": False, "final": False},
    ]
    trans_10 = [
        {"from": 0, "to": 4, "read": "Clean"},
        {"from": 0, "to": 1, "read": "Promo"},
        {"from": 0, "to": 2, "read": "Phish"},
        {"from": 1, "to": 2, "read": "Urgency"},
        {"from": 2, "to": 3, "read": "Phish"},
        {"from": 1, "to": 3, "read": "Bonus"},
    ]
    create_jff("experiment_10.jff", states_10, trans_10)

if __name__ == "__main__":
    build_all_10_experiments()
