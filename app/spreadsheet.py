# adapted from https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md

from dotenv import load_dotenv
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
load_dotenv()
#Custom function that returns a list of dictionaries from a google sheet
def get_spreadsheet(SHEET_NAME):
    """
    Provides access to a google sheet. It returns the google sheet from the unique website
    identifier that was input in the GOOGLE_SHEET_ID env variable.

    Requirements: Google API credentials service key saved as a .json file
    named google_api_credentials.json and downloaded into the folder named auth

    Returns: type = 'gspread.models.Worksheet'>
    """

    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    #SHEET_NAME = os.environ.get("SHEET_NAME", "Products")
    
    #CREDENTIALS_FILEPATH= os.environ.get("CREDENTIALS_FILE_PATH", "OOPS")
    
    #Accesses the filepath given you have downloaded the google sheets api credentials in the auth folder 
    #CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")
    
    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]
    #cred = json.loads(os.environ.get("CREDENTIALS_JSON","OOPS"))

   # credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    #credentials = ServiceAccountCredentials._from_parsed_json_keyfile(os.environ.get("CREDENTIALS_JSON","OOPS"),scopes='')
    #cred = json.loads(os.environ.get("CREDENTIALS_JSON","OOPS"))
    #credentials = service_account.Credentials.from_service_account_info(os.environ.get("CREDENTIALS_JSON","OOPS")
    creds =(os.environ.get("CREDENTIALS_JSON","OOPS"))
    
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds))
    #credentials = ServiceAccountCredentials.from_json_keyfile_dict(os.environ.get("CREDENTIALS_JSON","OOPS"))
    
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

   # print("\n--------------------------------")
    #print("SPREADSHEET:", doc.title)
    #print("--------------------------------\n")

    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    return sheet
   