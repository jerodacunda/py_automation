from src.logger import setup_logger
from src.ingestion import ingest_data
from src.cleaning import clean_data
from src.validation import validate_data, save_errors
from src.database import create_table, insert_data
import logging

logger = logging.getLogger(__name__)


def main():
    setup_logger()

    logger.info("Starting pipeline")

    file_path = "data/raw/properties.csv"

    # Pipeline
    data = ingest_data(file_path)
    clean = clean_data(data)
    valid, errors = validate_data(clean)

    # Logs
    logger.info(f"Valid rows: {len(valid)}")
    logger.info(f"Invalid rows: {len(errors)}")

    save_errors(errors)

    # DB
    create_table()
    insert_data(valid)

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()