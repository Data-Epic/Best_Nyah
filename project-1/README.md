# GSpread Workbook Utility

## Introduction

This Python script simplifies interactions with Google Sheets using the [gspread](https://gspread.readthedocs.io/en/latest/) library. Its main purpose is to create a Google Sheets spreadsheet, add a worksheet, populate it with CSV data, and share it with users.

## Prerequisites

1. **Service Account Credentials**: Obtain a Google Cloud Platform service account with the necessary Google Sheets permissions. Save the service account credentials as `credentials.json`.

2. **Python Libraries**: Install the required Python libraries in the `requirements/base.txt` file using pip:


## Process

- create & activate virtual environment: `virtualenv venv && source venv/bin/activate`

- create `.env` file for environment variables using `touch .env` 
    - define `EXTRACT_SH_PATH` variable with is absolute path to `extract.bash` script
  
- Install dependencies using `Make`:  `make install`

- run script using CLI: `python3 cli.py main --spread_sheet=,sheet_name> --csv_data_path=<your/file/directory.csv> --worksheet_name=<worksheet_name> --email=<email_to _share>`

  - example: `python3 cli.py main --spread_sheet=grocery_transactions1 --csv_data_path=./data/grocery_transactions.csv --worksheet_name=sheet2 --email=bestnyah7@gmail.com`

## Test
- **Unit Tests**: run with `make test`

output:
      [Link to spread sheet](https://docs.google.com/spreadsheets/d/1AkbhHTh-9HtWtNiGm4uEpJ3CTPv81f2CODeUkOkIGvs/edit?usp=sharing)


#### Libraries used
- fire: Python CLI creation.
- google-auth: Google Cloud Platform authentication.
- gspread: Google Sheets interaction.
- gspread-dataframe: Google Sheets to pandas.
- pandas: read csv file
- pytest: for unit & integration tests
- fastparquet: driver for parquet files
- python-decouple: read env variables