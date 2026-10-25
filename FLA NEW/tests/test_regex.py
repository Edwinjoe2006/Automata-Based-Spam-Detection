"""
Unit Tests for Formal Regex Patterns (10 Experiments)
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.regex_patterns import match_experiment_patterns, EXPERIMENTS


def test_exp01_free_pattern():
    res_pos = match_experiment_patterns("Claim your free gift today.")
    assert res_pos["flags"]["EXP01_FREE"] is True

    res_neg = match_experiment_patterns("The freeze warning was announced.")
    assert res_neg["flags"]["EXP01_FREE"] is False


def test_exp02_win_prize_pattern():
    res_pos1 = match_experiment_patterns("Congratulations, you won the draw!")
    assert res_pos1["flags"]["EXP02_WIN_PRIZE"] is True

    res_pos2 = match_experiment_patterns("Claim your cash prize now.")
    assert res_pos2["flags"]["EXP02_WIN_PRIZE"] is True

    res_neg = match_experiment_patterns("Please close the window.")
    assert res_neg["flags"]["EXP02_WIN_PRIZE"] is False


def test_exp03_urgent_pattern():
    res_pos = match_experiment_patterns("Urgent: your response is required.")
    assert res_pos["flags"]["EXP03_URGENT"] is True

    res_neg = match_experiment_patterns("Our project agent will visit.")
    assert res_neg["flags"]["EXP03_URGENT"] is False


def test_exp04_click_here_pattern():
    res_pos = match_experiment_patterns("Click here to see your reward.")
    assert res_pos["flags"]["EXP04_CLICK_HERE"] is True

    res_neg = match_experiment_patterns("Clock timer set for 10 minutes.")
    assert res_neg["flags"]["EXP04_CLICK_HERE"] is False


def test_exp05_suspicious_url_pattern():
    res_pos1 = match_experiment_patterns("Login at http://192.168.1.1/admin")
    assert res_pos1["flags"]["EXP05_SUSPICIOUS_URL"] is True

    res_pos2 = match_experiment_patterns("Visit https://claim-now.xyz for details")
    assert res_pos2["flags"]["EXP05_SUSPICIOUS_URL"] is True

    res_neg = match_experiment_patterns("Meeting in lab room 302.")
    assert res_neg["flags"]["EXP05_SUSPICIOUS_URL"] is False


def test_exp06_money_reward_pattern():
    res_pos = match_experiment_patterns("You won $5000 dollars bonus!")
    assert res_pos["flags"]["EXP06_MONEY_REWARD"] is True

    res_neg = match_experiment_patterns("The physics lab report is due.")
    assert res_neg["flags"]["EXP06_MONEY_REWARD"] is False


def test_exp07_account_verify_pattern():
    res_pos = match_experiment_patterns("Security alert: verify your account password.")
    assert res_pos["flags"]["EXP07_ACCOUNT_VERIFY"] is True

    res_neg = match_experiment_patterns("The syllabus was verified by the Dean.")
    assert res_neg["flags"]["EXP07_ACCOUNT_VERIFY"] is False


def test_exp08_exclamations_pattern():
    res_pos = match_experiment_patterns("Hurry up!! Don't wait!!!")
    assert res_pos["flags"]["EXP08_EXCLAMATIONS"] is True

    res_neg = match_experiment_patterns("Welcome to the course!")
    assert res_neg["flags"]["EXP08_EXCLAMATIONS"] is False


def test_exp09_multi_pattern():
    # 2 triggers (free + prize)
    res_pos = match_experiment_patterns("Free prize for all attendees.")
    assert res_pos["flags"]["EXP09_MULTI_PATTERN"] is True

    # 1 trigger (only free)
    res_neg = match_experiment_patterns("Free water available.")
    assert res_neg["flags"]["EXP09_MULTI_PATTERN"] is False
