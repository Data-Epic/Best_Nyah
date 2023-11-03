import pandas as pd
import gspread
from google.oauth2 import service_account
from decouple import config
from hijri_converter import Hijri
import re

CREDENTIALS_PATH = config("CREDENTIALS_PATH")

class CreateDataframeError(Exception):
    pass


def sheet_to_dataframe(url:str, worksheet_name:str) -> pd.DataFrame:

    scope = [
          "https://spreadsheets.google.com/feeds",
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive",
      ]

    try:
        # google cloud platform API credentials
        creds = service_account.Credentials.from_service_account_file(
            CREDENTIALS_PATH, scopes=scope
        )
        # create API client
        client = gspread.authorize(creds)

        # open worksheet based on name
        worksheet = client.open_by_url(url).worksheet(worksheet_name)
 
        # Load data from the worksheet into a Pandas DataFrame
        return pd.DataFrame(worksheet.get_all_records())

    except Exception as e:
          raise CreateDataframeError("Could not connect to Google Sheets") from e
    

