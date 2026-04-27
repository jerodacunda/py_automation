import sqlite3
import pandas as pd
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

DB_PATH = "data/database.db"


# ------------------------
# CONNECTION (context manager)
# ------------------------
@contextmanager
def get_connection(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        logger.error(f"Database error: {e}")
        raise
    finally:
        conn.close()


# ------------------------
# CREATE TABLE
# ------------------------
def create_table():
    logger.info("Creating table if not exists")

    query = """
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        price REAL NOT NULL,
        location TEXT NOT NULL,
        owner_name TEXT,
        rooms INTEGER,
        created_at TEXT
    );
    """

    with get_connection() as conn:
        conn.execute(query)


# ------------------------
# INSERT DATA
# ------------------------
def insert_data(df: pd.DataFrame):
    """
    Inserts valid data into SQLite.
    Uses INSERT OR IGNORE to avoid duplicate PK crashes.
    """

    if df.empty:
        logger.warning("No data to insert")
        return

    # Convert datetime to string (ISO format)
    df = df.copy()
    df["created_at"] = df["created_at"].astype(str)

    query = """
    INSERT OR IGNORE INTO properties (
        id, title, price, location, owner_name, rooms, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?);
    """

    data_tuples = list(df.itertuples(index=False, name=None))

    logger.info(f"Inserting {len(data_tuples)} rows into database")

    with get_connection() as conn:
        conn.executemany(query, data_tuples)

    logger.info("Insert completed")