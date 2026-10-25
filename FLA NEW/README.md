# Automata-Based Email Spam Detection and Classification Using Finite Automata and Regular Expressions

**Degree:** Bachelor of Technology in Information Technology (B.Tech IT)  
**Course Code & Name:** 21CSC301T &mdash; Formal Language and Automata  
**Target Subject:** 3rd Year Academic Laboratory & Theory Coursework  
**Tools:** Python 3, Flask, JFLAP 7.1, Scikit-learn, Pandas, NumPy, HTML5, CSS3, JavaScript  

---

## 📌 1. Project Overview

This project implements an academic, mathematically explainable email spam classification architecture grounded in **Formal Languages and Automata Theory (FLA)**. 

Rather than relying purely on machine learning black boxes, this system:
1. Formulates **10 discrete automata and regular expression experiments** designed in **JFLAP 7.1**.
2. Normalizes natural language text and extracts suspicious grammatical patterns.
3. Computes a deterministic spam risk score based on documented pattern weights.
4. Simulates an **Integrated Spam Decision Automaton** tracking step-by-step state trajectories.
5. Provides a comparative baseline using a **TF-IDF + Logistic Regression** machine learning model.

---

## 📁 2. Project Directory Layout

```text
FLA/
├── app.py                      # Flask web application entrypoint (5 interactive pages)
├── config.py                   # Central settings: paths, weights, threshold, column names
├── requirements.txt            # Python dependencies (flask, pandas, numpy, scikit-learn, pytest)
├── README.md                   # This comprehensive setup & submission guide
│
├── data/
│   ├── dataset.csv             # Cleaned Kaggle dataset (10,000 records)
│   └── README.md               # Dataset source citation and manual download steps
│
├── automata/                   # 10 JFLAP .jff XML models
│   ├── create_jff_files.py     # Automata generator script
│   ├── experiment_01.jff       # Exp 1: "FREE" keyword DFA
│   ├── experiment_02.jff       # Exp 2: "WIN" or "PRIZE" NFA/DFA
│   ├── experiment_03.jff       # Exp 3: "URGENT" or "ACT NOW" DFA
│   ├── experiment_04.jff       # Exp 4: "CLICK HERE" DFA
│   ├── experiment_05.jff       # Exp 5: Suspicious URL / IP pattern DFA
│   ├── experiment_06.jff       # Exp 6: Money / Currency / Cash pattern DFA
│   ├── experiment_07.jff       # Exp 7: Password / Security alert request DFA
│   ├── experiment_08.jff       # Exp 8: Repeated exclamation marks (!{2,}) DFA
│   ├── experiment_09.jff       # Exp 9: Multi-pattern threshold counter DFA
│   └── experiment_10.jff       # Exp 10: Integrated Spam Decision Automaton
│
├── jflap/
│   ├── JFLAP7.1.jar            # Runnable JFLAP 7.1 Java archive
│   ├── spam_dfa.jff            # Core DFA model
│   └── spam_nfa.jff            # Core NFA model
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py        # Case normalization, tokenization, dataset loader & validator
│   ├── regex_patterns.py       # Formal regex patterns and metadata for 10 experiments
│   ├── automata_engine.py      # State machine simulation engine tracking transitions
│   ├── classifier.py           # Rule-based weighted scoring engine + optional ML classifier
│   └── evaluation.py           # Metric calculation (Accuracy, Precision, Recall, F1, Confusion Matrix)
│
├── templates/
│   ├── base.html               # Master layout with responsive navbar & footer
│   ├── index.html              # Dashboard (dataset stats, live metrics, visual distribution)
│   ├── analyze.html            # Email Analyzer (interactive textarea, triggered rules, state traces)
│   ├── explorer.html           # Dataset Explorer (preview records, distribution, validation report)
│   ├── lab.html                # Automata Laboratory (10 experiments, transition tables, .jff download links)
│   └── evaluation.html         # Evaluation Page (Rule-Based vs ML comparison table, Confusion Matrix)
│
├── static/
│   ├── style.css               # Professional responsive CSS styling
│   └── script.js               # Frontend JavaScript interactions
│
├── tests/
│   ├── test_regex.py           # Unit tests verifying all 10 regex pattern rules
│   ├── test_classifier.py      # 20+ comprehensive test cases (Spam, Ham, URLs, Edge cases)
│   └── test_app.py             # Flask route testing (all 5 pages + API endpoints)
│
├── notebooks/
│   ├── generate_colab_notebook.py
│   └── spam_detection_colab.ipynb # Interactive Google Colab notebook (.ipynb)
│
├── results/
│   └── README.md               # Real evaluated metrics on 2,000 held-out test emails
│
└── reports/
    ├── report_outline.md       # 21-section Academic Project Report Outline
    └── viva_qa.md              # 10 Easy-to-memorize Viva Q&A
```

---

## ⚡ 3. Quick Local Execution Guide

### Step 1: Install Dependencies
Open terminal inside the `FLA/` directory:
```bash
cd "C:\Users\Edwin Joe\OneDrive\Documents\FLA"
pip install -r requirements.txt
```

### Step 2: Run Automated Test Suite (38 Tests)
```bash
pytest -v tests/
```
*(All 38 tests will execute and pass 100% successfully).*

### Step 3: Launch the Flask Web Application
```bash
python app.py
```
Open your browser and navigate to:
👉 **`http://127.0.0.1:5000`**

### Available Pages:
- **Dashboard (`/`):** Dataset summary (10,000 records), class distribution, and quick metrics.
- **Email Analyzer (`/analyze`):** Interactive email input with 6 quick samples, score meter, triggered rules, and state traces.
- **Dataset Explorer (`/explorer`):** CSV upload and validation, schema preview, and row validation.
- **Automata Lab (`/lab`):** 10 formal experiment tabs with transition tables and `.jff` download links.
- **Evaluation (`/evaluation`):** Real comparative metrics and confusion matrices on 2,000 held-out test emails.

---

## ☕ 4. How to Test in JFLAP 7.1

1. Double-click `jflap/JFLAP7.1.jar` inside `C:\Users\Edwin Joe\OneDrive\Documents\FLA\jflap\`.
2. In the JFLAP window, click **File → Open**.
3. Choose any `.jff` model from `automata/` or `jflap/`:
   - `experiment_01.jff` to `experiment_10.jff`
4. Test strings using:
   - **Input → Fast Run...** (Instant Accept/Reject)
   - **Input → Step with State...** (Animated state transitions)
   - **Input → Multiple Run** (Batch table execution)

---

## ☁️ 5. Google Colab Instructions

1. Open your browser and go to [Google Colab](https://colab.research.google.com/).
2. Click **Upload** and select `notebooks/spam_detection_colab.ipynb` from this project folder.
3. Run the cells sequentially to observe dataset loading, automata pattern matching, and comparative evaluation.
4. **How to Share with Faculty:**
   - Click the **Share** button in the top-right corner of Colab.
   - Set general access to *"Anyone with the link can view"* (or add faculty's email).
   - Copy the shareable link and include it in your project submission document.

---

## 🐙 6. GitHub Repository Upload Instructions

To upload this complete project to GitHub:

1. Open Command Prompt inside `C:\Users\Edwin Joe\OneDrive\Documents\FLA`:
   ```bash
   cd "C:\Users\Edwin Joe\OneDrive\Documents\FLA"
   ```
2. Initialize git repository:
   ```bash
   git init
   ```
3. Add all files to staging:
   ```bash
   git add .
   ```
4. Commit the project:
   ```bash
   git commit -m "Initial submission: Automata-Based Email Spam Detection Using Finite Automata and Regular Expressions"
   ```
5. Create a new repository on GitHub named `automata-spam-detection`.
6. Link remote and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/automata-spam-detection.git
   git branch -M main
   git push -u origin main
   ```

---

## 📋 7. Final Checklist for B.Tech Project Submission

- [x] **Verified Kaggle Dataset:** 10,000 records preserved in `data/dataset.csv`.
- [x] **10 JFLAP Automata Models:** Valid `.jff` XML files in `automata/`.
- [x] **Executable Code:** Flask app, preprocessing, regex engine, and rule-based classifier.
- [x] **Automated Tests:** 38 unit & integration tests passing via `pytest`.
- [x] **Empirical Results:** Documented in `results/README.md` (90.65% Rule-Based Accuracy on 2,000 emails).
- [x] **Google Colab Notebook:** Ready in `notebooks/spam_detection_colab.ipynb`.
- [x] **Academic Report:** 21-section report outline populated in `reports/report_outline.md`.
- [x] **Viva Q&A:** 10 concise questions and answers ready in `viva_qa.md`.
