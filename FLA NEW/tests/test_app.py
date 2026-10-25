"""
Flask Web Application Integration Tests
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib.util

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_file = os.path.join(project_root, "app.py")
spec = importlib.util.spec_from_file_location("main_app", app_file)
main_app = importlib.util.module_from_spec(spec)
sys.modules["main_app"] = main_app
spec.loader.exec_module(main_app)
app = main_app.app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_dashboard_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Automata-Based Email Spam Detection" in response.data


def test_analyze_route_get(client):
    response = client.get("/analyze")
    assert response.status_code == 200
    assert b"Automata-Based Email Analyzer" in response.data


def test_analyze_route_post(client):
    response = client.post("/analyze", data={
        "email_text": "Congratulations! You won a free prize. Click here now!",
        "threshold": "40"
    })
    assert response.status_code == 200
    assert b"SPAM" in response.data
    assert b"Risk Score" in response.data


def test_explorer_route_get(client):
    response = client.get("/explorer")
    assert response.status_code == 200
    assert b"Dataset Explorer & Schema Validator" in response.data


def test_lab_route(client):
    response = client.get("/lab")
    assert response.status_code == 200
    assert b"Automata Laboratory" in response.data
    assert b"EXP01" in response.data
    assert b"EXP10" in response.data


def test_evaluation_route(client):
    response = client.get("/evaluation")
    assert response.status_code == 200
    assert b"Comparative Model Evaluation" in response.data
    assert b"Confusion Matrix" in response.data


def test_download_jff_route(client):
    response = client.get("/download/experiment_01.jff")
    assert response.status_code == 200
    assert b"<structure>" in response.data


def test_api_classify_endpoint(client):
    response = client.post("/api/classify", json={
        "text": "Meeting tomorrow at 10 AM regarding project report."
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["verdict"] == "HAM"
    assert data["is_spam"] is False
