import pandas as pd
import logging

logger = logging.getLogger(__name__)


def ingest_data(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a DataFrame with required columns.
    """

    logger.info(f"Reading file: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded {len(df)} rows")

        return df

    except Exception as e:
        logger.error(f"Error ingesting data: {e}")
        raise