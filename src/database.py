import sqlite3
import pandas as pd
from contextlib import contextmanager


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
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ------------------------
# CREATE TABLE
# ------------------------
def create_table():
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
        print("No data to insert.")
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

    with get_connection() as conn:
        conn.executemany(query, data_tuples)

    print(f"Inserted {len(data_tuples)} rows (duplicates ignored).")