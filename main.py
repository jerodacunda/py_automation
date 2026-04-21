from src.ingestion import ingest_data
from src.cleaning import clean_data
from src.validation import validate_data, save_errors
from src.database import create_table, insert_data


def main():
    file_path = "data/raw/properties.csv"

    # Pipeline
    data = ingest_data(file_path)
    clean = clean_data(data)
    valid, errors = validate_data(clean)

    # Logs
    print(f"Valid rows: {len(valid)}")
    print(f"Invalid rows: {len(errors)}")

    save_errors(errors)

    # DB
    create_table()
    insert_data(valid)


if __name__ == "__main__":
    main()