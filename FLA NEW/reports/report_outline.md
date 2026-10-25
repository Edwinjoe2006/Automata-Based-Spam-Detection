# Academic Project Report Outline
## B.Tech Information Technology &bull; Third Year
### Course Code: 21CSC301T &mdash; Formal Language and Automata
### Project Title: Automata-Based Email Spam Detection and Classification Using Finite Automata and Regular Expressions

---

### 1. Title Page
- **Project Title:** Automata-Based Email Spam Detection and Classification Using Finite Automata and Regular Expressions
- **Degree:** Bachelor of Technology in Information Technology (B.Tech IT)
- **Course Name & Code:** Formal Language and Automata (21CSC301T)
- **Academic Year:** 2026-2027
- **Software Tools Used:** Python 3, Flask, JFLAP 7.1, Scikit-learn, Pandas, NumPy, HTML5/CSS3/JavaScript

---

### 2. Abstract
Spam emails pose a severe security, operational, and bandwidth hazard to modern digital infrastructure. While industry filters predominantly employ deep neural networks or statistical classifiers operating as mathematical black boxes, this academic project develops an explainable, deterministic email spam classification architecture grounded in Formal Languages and Automata Theory (FLA). We formulate 10 formal regular language pattern recognizers using Deterministic Finite Automata (DFA), Non-deterministic Finite Automata (NFA), and Regular Expressions (Regex), designed and validated in JFLAP 7.1. Incoming email text is normalized and evaluated against a weighted automata decision engine that maps pattern triggers to discrete state trajectories. Evaluated on a 10,000-email Kaggle dataset, the rule-based automata filter achieves **90.65% accuracy** and **100% precision** on a 2,000 held-out test split, maintaining an ultra-lightweight linear time complexity of $O(N)$ without the energy or computational overhead of machine learning training.

---

### 3. Introduction
Formal Language and Automata Theory represents the foundational science of computer engineering, defining the mathematical limits of language recognition and state computation. A Finite State Machine (FSM) computes membership of a string $w$ in a formal language $L \subseteq \Sigma^*$. While modern spam filtering has skewed toward machine learning, automata theory offers unrivaled advantages in deterministic predictability, zero-latency execution, and complete verifiability. This project demonstrates how classical theoretical computer science concepts can be directly engineered into practical email security software.

---

### 4. Problem Statement
Commercial machine learning spam filters require thousands of labeled training records, continuous hyperparameter tuning, GPU computational clusters, and offer zero explainability for why an individual message was flagged. The core problem addressed is: *How can an email classification system be constructed using deterministic finite automata and regular expressions such that every classification decision is backed by a verifiable state transition trajectory in JFLAP?*

---

### 5. Objectives
1. Design and simulate 10 discrete automata and regular expression experiments in JFLAP 7.1.
2. Define formal alphabets $\Sigma$, regular expressions $r$, and state transition functions $\delta(q, a)$ for email spam heuristics.
3. Engineer an automated text normalization and tokenization pipeline in Python.
4. Implement an independent, rule-based weighted risk engine with an Integrated Spam Decision Automaton.
5. Build an optional TF-IDF + Logistic Regression model to provide a genuine academic baseline comparison.
6. Develop a 5-page responsive Flask web application (Dashboard, Email Analyzer, Dataset Explorer, Automata Lab, and Evaluation).
7. Validate the architecture using 20+ documented unit test cases and 2,000 held-out test emails.

---

### 6. Literature Review
- **Chomsky's Hierarchy (1956):** Established Regular Languages (Type 3) as recognizable by Finite State Automata.
- **Hopcroft, Motwani, & Ullman (2006):** Detailed the mathematical equivalence of Regular Expressions, Non-deterministic Finite Automata, and Deterministic Finite Automata via Subset Construction.
- **Rodger & Finley (2006):** Developed JFLAP as an interactive graphical simulator for formal languages and automata.
- **Modern Text Filtering:** Compares lexical automata scanners (Aho-Corasick, DFA lexers) with probabilistic models (Naive Bayes, SVM, BERT).

---

### 7. Research Area
- **Primary Domain:** Theoretical Computer Science / Formal Languages and Automata Theory (FLA).
- **Secondary Domain:** Natural Language Processing (Lexical Analysis & Tokenization) and Cyber-Security (Phishing and Spam Mitigation).

---

### 8. Dataset Description and Source
- **Kaggle Source:** [Spam Email Detection Dataset (Clean & ML Ready)](https://www.kaggle.com/datasets/ssssws/spam-email-detection-dataset-clean-and-ml-ready) by Thanh Nhan Nguyen (`ssssws`).
- **File Name:** `spam_email_dataset.csv` (active location: `data/dataset.csv`).
- **Volume:** 10,000 email records.
- **Spam Records (1):** 3,995 (39.95%).
- **Ham Records (0):** 6,005 (60.05%).
- **Attributes:** `email_text` (body content) and `label` (binary classification).

---

### 9. Formal Language Definitions
The system models spam indicators as regular languages over alphabets $\Sigma$:
- **Experiment 1 (Promotional):** $L_1 = \{ w \in \Sigma^* \mid w \text{ contains token 'FREE'} \}$
- **Experiment 2 (Contest/Prize):** $L_2 = \{ w \in \Sigma^* \mid w \text{ contains 'WIN' or 'PRIZE'} \}$
- **Experiment 3 (Urgency):** $L_3 = \{ w \in \Sigma^* \mid w \text{ contains 'URGENT' or 'ACT NOW'} \}$
- **Experiment 4 (Call to Action):** $L_4 = \{ w \in \Sigma^* \mid w \text{ contains 'CLICK HERE'} \}$
- **Experiment 5 (Hyperlinks):** $L_5 = \{ w \in \Sigma^* \mid w \text{ contains 'http://' or raw IP address} \}$
- **Experiment 6 (Financial):** $L_6 = \{ w \in \Sigma^* \mid w \text{ contains currency symbol and numerical amount} \}$
- **Experiment 7 (Phishing):** $L_7 = \{ w \in \Sigma^* \mid w \text{ contains 'VERIFY ACCOUNT' or 'SECURITY ALERT'} \}$
- **Experiment 8 (Punctuation):** $L_8 = \{ w \in \{!, \neg!\}^* \mid w \text{ contains consecutive '!'} \}$
- **Experiment 9 (Synergy Counter):** $L_9 = \{ w \in \Gamma^* \mid |w| \ge 2 \text{ distinct triggers} \}$
- **Experiment 10 (Integrated Language):** $L_{10} = \text{Emails traversing to terminal state } Q_{SPAM}$.

---

### 10. Regular Expressions
| Exp | Target Heuristic | Formal Regular Expression ($r$) |
| :-: | :--- | :--- |
| **01** | Promotional Lure | `\b(free\|freebie\|complimentary)\b` |
| **02** | Victory / Contest | `\b(win\|winner\|won\|winning\|prize\|reward\|jackpot)\b` |
| **03** | Urgency Manipulation | `\b(urgent\|urgently\|act now\|expires? today\|immediate action)\b` |
| **04** | Action Directives | `\b(click here\|click link\|click below\|tap here)\b` |
| **05** | Suspicious URLs | `(https?://\S+\|www\.\S+\|\b\d{1,3}(\.\d{1,3}){3}\b)` |
| **06** | Currency / Bounty | `(\$\s*\d+\|\b\d+\s*(dollars?\|usd\|cash\|bonus)\b)` |
| **07** | Account Phishing | `\b(verify (your )?account\|security alert\|reset (your )?password)\b` |
| **08** | Punctuation Abuse | `!{2,}` |
| **09** | Multi-Pattern Trigger | Aggregated threshold counter over trigger alphabet $\Gamma$ |
| **10** | Integrated Machine | Multi-stage regular rule graph |

---

### 11. DFA/NFA Design and Transition Tables
*(Refer to `automata/` directory for full JFLAP XML models)*
- **5-Tuple Model:** $M = (Q, \Sigma, \delta, q_0, F)$
- Example Transition Table for Exp 08 (Exclamation Abuse DFA):
  - $\delta(q_0, !) = q_1$, $\delta(q_0, \text{other}) = q_0$
  - $\delta(q_1, !) = q_2$ (Accepting), $\delta(q_1, \text{other}) = q_0$
  - $\delta(q_2, !) = q_2$, $\delta(q_2, \text{other}) = q_2$

---

### 12. System Architecture
```
Raw Email Input
      │
      ▼
Text Normalization & Tokenization (src/preprocessing.py)
      │
      ▼
10 Automata Pattern Recognizers (src/regex_patterns.py)
      │
      ├──> Pattern Weights & Risk Score Summation
      │
      ▼
Integrated Decision Automaton (src/automata_engine.py)
      │
      ▼
Final Classification (SPAM / HAM) + Deterministic Explanation (src/classifier.py)
      │
      ▼
Flask Presentation Layer (templates/ + static/)
```

---

### 13. Algorithm and Pseudocode
```text
Algorithm: Automata_Spam_Classifier(email_text, threshold = 40)
Input: Raw string email_text, integer threshold
Output: Classification dictionary (verdict, risk_score, triggered_rules, state_trace)

1. normalized_text = NormalizeWhitespaceAndCase(email_text)
2. If normalized_text is empty:
      Return HAM (score = 0)
3. Initialize total_score = 0, triggered_rules = []
4. For each experiment E in [EXP01 ... EXP08]:
      If E.regex matches normalized_text:
         total_score += E.weight
         Append E to triggered_rules
5. If count(triggered_rules) >= 2:
      total_score += 15 (EXP09 Multi-Pattern Synergy)
      Append EXP09 to triggered_rules
6. state_trace = SimulateIntegratedAutomaton(triggered_rules)
7. If total_score >= threshold:
      verdict = "SPAM"
   Else:
      verdict = "HAM"
8. Return {verdict, total_score, triggered_rules, state_trace}
```

---

### 14. Implementation Details
- **Backend:** Flask web server with modular `src/` hierarchy.
- **Frontend:** Semantic HTML5, CSS custom properties, and JavaScript.
- **Automata Validation:** JFLAP 7.1 XML schema compliance verified via `xml.etree.ElementTree`.
- **Machine Learning Module:** Scikit-learn TF-IDF vectorizer (2,500 n-grams) + LogisticRegression ($C=1.0$).

---

### 15. JFLAP Screenshots Checklist
*(Use these exact files in JFLAP 7.1 for lab manual screenshots)*
- [ ] **Screenshot 1:** `experiment_01.jff` &mdash; State canvas showing $q_0 \to q_4$.
- [ ] **Screenshot 2:** `experiment_02.jff` &mdash; NFA branching for "WIN" and "PRIZE".
- [ ] **Screenshot 3:** `experiment_03.jff` &mdash; Sequential DFA for "URGENT".
- [ ] **Screenshot 4:** `experiment_04.jff` &mdash; DFA for "CLICK HERE".
- [ ] **Screenshot 5:** `experiment_05.jff` &mdash; Protocol scanner for "http://".
- [ ] **Screenshot 6:** `experiment_08.jff` &mdash; Punctuation counter showing loop on $q_2$.
- [ ] **Screenshot 7:** Fast Run test showing green `Accept` dialog for `WWFP`.
- [ ] **Screenshot 8:** Step with State animation stepping through symbol tape.
- [ ] **Screenshot 9:** Multiple Run table with 10 test strings evaluated simultaneously.

---

### 16. Test Cases and Results (20+ Cases)
All 20 test cases verified via automated `pytest` test suite:
- 5/5 Legitimate Ham emails $\to$ **100% Correctly Classified as HAM**.
- 5/5 Obvious Spam emails $\to$ **100% Correctly Classified as SPAM**.
- 2/2 Suspicious URL & Phishing emails $\to$ **100% Correctly Classified as SPAM**.
- 2/2 Mixed Edge Case emails $\to$ **Correctly Classified as HAM** (isolated word didn't cross threshold).
- 2/2 Empty / Whitespace emails $\to$ **Safely Defaulted to HAM**.
- 2/2 Obfuscated / Punctuation abuse emails $\to$ **100% Correctly Classified as SPAM**.
- 2/2 Multi-pattern boundary emails $\to$ **100% Correctly Classified as SPAM**.

---

### 17. Evaluation Metrics (N = 2,000 Held-Out Emails)
- **Rule-Based Automata Accuracy:** **90.65%**
- **Rule-Based Precision:** **100.00%** (Zero False Positives)
- **Rule-Based Recall:** **76.60%**
- **Rule-Based F1-Score:** **86.75%**
- **ML Baseline Accuracy:** **100.00%**

---

### 18. Discussion and Limitations
- **Determinism:** Automata guarantee that the same input always yields identical state trajectories.
- **Zero False Positives:** Safe business and academic correspondence is protected from inadvertent quarantine.
- **Limitation:** Keyword heuristics cannot detect novel paraphrasing or image-based spam.

---

### 19. Future Enhancements
1. Implement a Pushdown Automaton (PDA) to parse nested HTML email DOM structures.
2. Integrate approximate string matching (Levenshtein distance) within automata transitions.
3. Deploy as a lightweight milter plugin at network mail gateways.

---

### 20. Conclusion
This project demonstrates that Formal Languages and Automata Theory provides a robust, computationally efficient, and mathematically transparent foundation for email spam detection. By transitioning from statistical black boxes to deterministic state machines, email classification can be rigorously analyzed, verified, and demonstrated in JFLAP.

---

### 21. References
1. Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3rd ed.). Pearson.
2. Linz, P. (2016). *An Introduction to Formal Languages and Automata* (6th ed.). Jones & Bartlett Learning.
3. Rodger, S. H., & Finley, T. W. (2006). *JFLAP: An Interactive Formal Languages and Automata Package*. Jones & Bartlett Learning.
4. Kaggle Dataset: `ssssws/spam-email-detection-dataset-clean-and-ml-ready` (2026).
