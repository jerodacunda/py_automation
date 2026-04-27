import pandas as pd
import logging

logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw data:
    - Handles missing values
    - Converts data types
    - Normalizes strings
    """
    logger.info("Starting data cleaning")

    df = df.copy()

    # ------------------------
    # 1. PRICE
    # ------------------------
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # ------------------------
    # 2. ROOMS
    # ------------------------
    df["rooms"] = pd.to_numeric(df["rooms"], errors="coerce")

    # ------------------------
    # 3. OWNER NAME
    # ------------------------
    missing_owner = df["owner_name"].isna().sum()
    if missing_owner:
        logger.warning(f"{missing_owner} rows missing owner_name")

    df["owner_name"] = df["owner_name"].fillna("UNKNOWN")

    # ------------------------
    # 4. TITLE & LOCATION
    # ------------------------
    df["title"] = df["title"].str.strip()
    df["location"] = df["location"].str.strip()

    # ------------------------
    # 5. CREATED_AT
    # ------------------------
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    logger.info("Finished data cleaning")

    return df