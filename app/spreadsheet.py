# adapted from https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md

from dotenv import load_dotenv
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


#Custom function that returns a list of dictionaries from a google sheet
def get_spreadsheet(SHEET_NAME,sheet_num):
    """
    Provides access to a google sheet. It returns the google sheet from the unique website
    identifier that was input in the GOOGLE_SHEET_ID env variable.

    Requirements: Google API credentials service key saved as a .json file
    named google_api_credentials.json and downloaded into the folder named auth

    Returns: type = 'gspread.models.Worksheet'>
    """

    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
    output_id = os.environ.get("NEW_SHEET_ID", "OOPS")
    
    #SHEET_NAME = os.environ.get("SHEET_NAME", "Products")

    #Accesses the filepath given you have downloaded the google sheets api credentials in the auth folder 
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")
    
    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

    #
    # READ SHEET VALUES
    #

    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>
  
    if sheet_num==2:
        
        doc = client.open_by_key(output_id) #> <class 'gspread.models.Spreadsheet'>
        
    else:
        doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>
        

   # print("\n--------------------------------")
    #print("SPREADSHEET:", doc.title)
    #print("--------------------------------\n")
    
    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    return sheet
   