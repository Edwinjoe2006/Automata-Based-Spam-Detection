"""
Preprocessing and Dataset Loading Module
B.Tech IT - Formal Language and Automata (21CSC301T)
"""

import os
import re
import pandas as pd
import numpy as np

import sys
# Ensure FLA root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config


def normalize_text(text: str) -> str:
    """
    Cleans raw email text:
    - Replaces newlines and tabs with spaces.
    - Strips leading and trailing whitespaces.
    - Preserves case for regex checks where case might matter,
      but collapses consecutive whitespace into a single space.
    """
    if not isinstance(text, str):
        return ""
    # Normalize whitespaces
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned


def tokenize_words(text: str) -> list:
    """
    Tokenizes normalized text into sequential word tokens.
    """
    if not text:
        return []
    return re.findall(r"\b\w+\b", text)


def load_dataset(csv_path: str = None) -> tuple:
    """
    Loads, cleans, and normalizes the dataset.
    Returns:
        tuple: (df, stats_dict)
    """
    if csv_path is None:
        csv_path = config.DATASET_PATH

    # Check if real CSV dataset exists
    if not os.path.exists(csv_path):
        # Fallback to Demo Data
        df = pd.DataFrame(config.DEMO_DATA)
        df["text"] = df["text"].apply(normalize_text)
        stats = {
            "source": "Built-in Demo Sample Data",
            "is_demo": True,
            "total_records": len(df),
            "spam_count": int((df["label"] == 1).sum()),
            "ham_count": int((df["label"] == 0).sum()),
            "spam_pct": round((df["label"] == 1).mean() * 100, 2),
            "ham_pct": round((df["label"] == 0).mean() * 100, 2),
            "file_name": "Demo Mode (10 records)",
            "text_column": "text",
            "label_column": "label"
        }
        return df, stats

    # Load actual CSV
    raw_df = pd.read_csv(csv_path)

    # 1. Dynamically find text column
    text_col = None
    for col in config.TEXT_COLUMN_CANDIDATES:
        if col in raw_df.columns:
            text_col = col
            break
    if not text_col:
        # Fallback: first object/string column
        obj_cols = [c for c in raw_df.columns if raw_df[c].dtype == "object"]
        text_col = obj_cols[0] if obj_cols else raw_df.columns[0]

    # 2. Dynamically find label column
    label_col = None
    for col in config.LABEL_COLUMN_CANDIDATES:
        if col in raw_df.columns:
            label_col = col
            break
    if not label_col:
        for c in raw_df.columns:
            if raw_df[c].nunique() == 2:
                label_col = c
                break
    if not label_col:
        label_col = raw_df.columns[-1]

    initial_count = len(raw_df)

    # 3. Clean missing values and whitespace
    cleaned_df = raw_df.dropna(subset=[text_col, label_col]).copy()
    cleaned_df["text"] = cleaned_df[text_col].astype(str).apply(normalize_text)

    # Drop empty texts after cleaning
    cleaned_df = cleaned_df[cleaned_df["text"].str.len() > 0]

    # 4. Normalize labels to integer 1 (Spam) and 0 (Ham)
    def map_label(val):
        if val in config.LABEL_NORMALIZATION:
            return config.LABEL_NORMALIZATION[val]
        val_str = str(val).strip().lower()
        if val_str in config.LABEL_NORMALIZATION:
            return config.LABEL_NORMALIZATION[val_str]
        return 0  # Default to Ham if ambiguous

    cleaned_df["label"] = cleaned_df[label_col].apply(map_label)

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    total_records = len(cleaned_df)
    spam_count = int((cleaned_df["label"] == 1).sum())
    ham_count = int((cleaned_df["label"] == 0).sum())
    spam_pct = round((spam_count / total_records) * 100, 2) if total_records > 0 else 0
    ham_pct = round((ham_count / total_records) * 100, 2) if total_records > 0 else 0

    stats = {
        "source": "Kaggle Verified CSV",
        "is_demo": False,
        "kaggle_url": config.DATASET_KAGGLE_URL,
        "file_name": os.path.basename(csv_path),
        "raw_records": initial_count,
        "total_records": total_records,
        "spam_count": spam_count,
        "ham_count": ham_count,
        "spam_pct": spam_pct,
        "ham_pct": ham_pct,
        "text_column": text_col,
        "label_column": label_col,
        "columns": list(raw_df.columns)
    }

    return cleaned_df[["text", "label"]], stats


def validate_uploaded_csv(file_path: str) -> dict:
    """
    Validates an uploaded CSV file for dataset explorer.
    """
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return {"valid": False, "error": f"Failed to parse CSV: {str(e)}"}

    total_rows = len(df)
    columns = list(df.columns)

    # Substring / fuzzy column matching
    text_col = None
    for c in columns:
        c_lower = c.lower()
        if any(cand in c_lower for cand in ["text", "body", "content", "message", "email"]):
            text_col = c
            break
    if not text_col and columns:
        # Fallback to first text column
        obj_cols = [c for c in df.columns if df[c].dtype == "object"]
        text_col = obj_cols[0] if obj_cols else columns[0]

    label_col = None
    for c in columns:
        c_lower = c.lower()
        if any(cand in c_lower for cand in ["label", "class", "target", "spam", "category"]):
            label_col = c
            break
    if not label_col and len(columns) > 1:
        # Fallback to last column
        label_col = columns[-1]

    missing_text = int(df[text_col].isna().sum()) if text_col else total_rows
    missing_label = int(df[label_col].isna().sum()) if label_col else total_rows

    preview_rows = df.head(10).to_dict(orient="records")

    return {
        "valid": bool(text_col and label_col),
        "total_rows": total_rows,
        "columns": columns,
        "text_column": text_col,
        "label_column": label_col,
        "missing_text_count": missing_text,
        "missing_label_count": missing_label,
        "preview": preview_rows
    }
