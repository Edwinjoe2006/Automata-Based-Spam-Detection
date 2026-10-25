# Project Evaluation Results & Experimental Findings
## Course: Formal Language and Automata (21CSC301T)

---

## 1. Experimental Methodology
- **Dataset:** 10,000 emails from Kaggle (`ssssws/spam-email-detection-dataset-clean-and-ml-ready`)
- **Evaluation Split:** 80% Training (8,000 emails) &bull; 20% Held-Out Testing (2,000 emails)
- **Class Balance in Test Set:** 1,201 Ham (60.05%) &bull; 799 Spam (39.95%)
- **Target Comparison:** Deterministic Rule-Based Automata Engine vs Statistical TF-IDF + Logistic Regression

---

## 2. Quantitative Evaluation Table

| Evaluation Metric | Rule-Based Automata Engine (Primary) | Machine Learning Benchmark (Comparative) |
| :--- | :---: | :---: |
| **Model Type** | Finite State Automata & Regular Expressions | TF-IDF (2,500 n-grams) + Logistic Regression |
| **Test Set Size** | 2,000 emails | 2,000 emails |
| **Accuracy** | **90.65%** | **100.00%** |
| **Precision (Spam)** | **100.00%** | **100.00%** |
| **Recall (Spam)** | **76.60%** | **100.00%** |
| **F1-Score (Spam)** | **86.75%** | **100.00%** |
| **Execution Time** | **< 1 ms per email** | **~ 8 ms per email** |
| **Explainability** | **100% Deterministic State Proof** | **Statistical Weights (Probabilistic)** |

---

## 3. Confusion Matrix Breakdown (N = 2,000)

### A. Rule-Based Automata Engine
- **True Negatives (TN):** 1,201 (All 1,201 legitimate emails were correctly identified as HAM)
- **False Positives (FP):** 0 (Zero legitimate emails were falsely flagged as spam!)
- **False Negatives (FN):** 187 (Spam messages that evaded the 10 predefined keyword heuristics)
- **True Positives (TP):** 612 (Spam emails correctly captured by the automata rules)

### B. Machine Learning Baseline
- **True Negatives (TN):** 1,201
- **False Positives (FP):** 0
- **False Negatives (FN):** 0
- **True Positives (TP):** 799

---

## 4. Key Academic Insights for Viva
1. **Zero False Positives:** The Rule-Based Automata engine achieved a 100% precision score on the test set, meaning when an email is flagged as SPAM by the automata, it is guaranteed to contain verifiable malicious triggers.
2. **Deterministic Transparency:** Unlike the ML model where decisions are opaque matrix multiplications, every classification in the automata engine maps to a specific state trajectory in JFLAP (e.g., $q_0 \to q_1 \to q_2 \dots$).
3. **Efficiency:** The finite automaton runs in strict linear time $O(N)$ with no matrix computation or GPU requirement.
