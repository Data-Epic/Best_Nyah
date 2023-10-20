from pathlib import Path
from google.oauth2 import service_account
from gspread_dataframe import set_with_dataframe
import gspread
import pandas as pd
import logging


# logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)


class DataPopulationError(Exception):
    pass


class NewSheetError(Exception):
    pass


class NewSpreadsheetError(Exception):
    pass


class Workbook:
    #  initialize gspread connections
    def __init__(
        self, workbook_name: str, csv_file: Path, sheet_name: str, email: str
    ) -> None:
        self.workbook_name = workbook_name
        self.csv_file = csv_file
        self.sheet_name = sheet_name
        self.email = email

        self.df = pd.read_csv(self.csv_file)

        # connection parameters
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive",
        ]

        try:
            # google cloud platform API credentials
            creds = service_account.Credentials.from_service_account_file(
                "./credentials.json", scopes=scope
            )
            # create API client
            self.client = gspread.authorize(creds)

            logging.info("Connected to Google Sheets successfully.")
        except Exception as e:
            logging.error(f"Could not connect to Google Sheets: {e}")

    # create a new spread sheet & add email to share
    def create_new_spreadsheet(self) -> None:
        try:
            # create new workbook/spreadsheet
            self.sh = self.client.create(self.workbook_name)

            # add email to share view/roles
            self.sh.share(self.email, perm_type="user", role="writer")

            logging.info(
                f"New spreadsheet '{self.workbook_name}' created successfully."
            )
            return self.sh

        except Exception as e:
            logging.error(f"Error creating a new spreadsheet: {e}")
            raise NewSpreadsheetError("Error creating a new spreadsheet") from e

    # create new work sheet from spreadsheet
    def create_new_sheet(self) -> None:
        try:
            self.worksheet = self.sh.add_worksheet(
                self.sheet_name, self.df.shape[0], self.df.shape[1]
            )
            logging.info(f"New sheet '{self.sheet_name}' created successfully.")

        except Exception as e:
            logging.error(f"Error creating a new sheet: {e}")
            raise NewSheetError("Error creating a new sheet") from e

    def populate_sheet_from_csv(self) -> None:
        try:
            set_with_dataframe(self.worksheet, self.df)
            logging.info("Data populated in the sheet successfully.")
        except Exception as e:
            logging.error(f"Error populating sheet from CSV: {e}")
            raise DataPopulationError("Error populating sheet from CSV") from e


def main(
    spread_sheet: str, csv_data_path: Path, worksheet_name: str, email: str
) -> None:
    wb = Workbook(spread_sheet, csv_data_path, worksheet_name, email)
    wb.create_new_spreadsheet()
    wb.create_new_sheet()
    wb.populate_sheet_from_csv()
