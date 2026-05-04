# Data Processing & Automation Pipeline

Data pipeline built in Python that ingests CSV data, performs cleaning and validation, and stores results in a SQLite database. 

---

## Features

- CSV data ingestion with schema validation
- Data cleaning (type conversion, null handling, normalization)
- Row-level validation with detailed error tracking
- Structured logging (file + console, multiple levels)
- SQLite persistence with batch inserts

---

## Project Structure

```
│
├── main.py
│
├── data/
│ ├── raw/
│ └── processed/
│
├── logs/
│
├── src/
│ ├── ingestion.py
│ ├── cleaning.py
│ ├── validation.py
│ ├── database.py
│ └── logger.py
│
└── tests/
```

---

## Pipeline Overview

1. **Ingestion**
   - Reads CSV input
   - Validates required columns

2. **Cleaning**
   - Handles missing values
   - Converts data types
   - Normalizes strings

3. **Validation**
   - Applies business rules
   - Separates valid and invalid records
   - Logs errors per row

4. **Persistence**
   - Inserts valid records into SQLite database
   - Uses batch operations and duplicate handling

5. **Logging**
   - Structured logs with levels (INFO, WARNING, ERROR)
   - Output to console and file (`logs/pipeline.log`)

---

## Example Output

- Valid records → inserted into database
- Invalid records → saved to `logs/errors.csv`
- Execution logs → `logs/pipeline.log`

---
