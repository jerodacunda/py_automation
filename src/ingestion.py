import pandas as pd


REQUIRED_COLUMNS = [
    "id",
    "title",
    "price",
    "location",
    "owner_name",
    "rooms",
    "created_at",
]


def ingest_data(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and returns a DataFrame with required columns.
    """

    try:
        df = pd.read_csv(file_path)

        # Validar que estén las columnas necesarias
        missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")

        # Filtrar solo columnas necesarias
        df = df[REQUIRED_COLUMNS]

        return df

    except Exception as e:
        raise RuntimeError(f"Error ingesting data: {e}")