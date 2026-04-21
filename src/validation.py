import pandas as pd
from typing import Tuple, List, Dict


def validate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Validates cleaned data and separates valid and invalid rows.

    Returns:
        valid_df: rows that passed validation
        error_df: rows with validation errors + error details
    """

    valid_rows = []
    error_rows = []

    for index, row in df.iterrows():
        errors = []

        # ------------------------
        # RULES
        # ------------------------

        # 1. price must exist and be > 0
        if pd.isna(row["price"]) or row["price"] <= 0:
            errors.append("Invalid price")

        # 2. rooms must exist and be > 0
        if pd.isna(row["rooms"]) or row["rooms"] <= 0:
            errors.append("Invalid rooms")

        # 3. created_at must be valid
        if pd.isna(row["created_at"]):
            errors.append("Invalid date")

        # 4. title must not be empty
        if not row["title"] or str(row["title"]).strip() == "":
            errors.append("Empty title")

        # 5. location must not be empty
        if not row["location"] or str(row["location"]).strip() == "":
            errors.append("Empty location")

        # ------------------------
        # RESULT
        # ------------------------

        if errors:
            error_entry = row.to_dict()
            error_entry["errors"] = "; ".join(errors)
            error_rows.append(error_entry)
        else:
            valid_rows.append(row)

    valid_df = pd.DataFrame(valid_rows)
    error_df = pd.DataFrame(error_rows)

    return valid_df, error_df

def save_errors(error_df: pd.DataFrame, path: str = "logs/errors.csv"):
    if not error_df.empty:
        error_df.to_csv(path, index=False)