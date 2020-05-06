# adapted from https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md

from dotenv import load_dotenv
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


#Custom function that returns a google sheet
def get_spreadsheet(SHEET_NAME,sheet_num=0):
    """
    Provides access to a google sheet. It returns the google sheet from the unique website
    identifier that was input in the GOOGLE_SHEET_ID env variable.

    Requirements: Google API credentials service key saved as a .json file
    named google_api_credentials.json and downloaded into the folder named auth

    Params: SHEET_NAME(string), sheet_num(integer)

    Example: get_spreadsheet("Starbucks",1)
    Returns: type = 'gspread.models.Worksheet'>
    """

    DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")


    #Accesses the filepath given you have downloaded the google sheets api credentials in the auth folder 
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")
    
    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)


    client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>
    
    #Depending on what restaurant was chosen this is where the code is output to
    """
    Note: These are based on the restaurant identifiers in the env file. If your restaurant output
    sheets differ, then these must be changed in order to reflect the sheet ID's. Must make corresponding
    change in the homeroutes create_user() function as well
    """
    if sheet_num==1:
        DOCUMENT_ID = os.environ.get("STARBUCKS_SHEET_ID", "OOPS")
    elif sheet_num==2:
        DOCUMENT_ID = os.environ.get("CFA_SHEET_ID", "OOPS")
    elif sheet_num==3:
        DOCUMENT_ID = os.environ.get("WISEYS_SHEET_ID", "OOPS")
    elif sheet_num==4:
        DOCUMENT_ID = os.environ.get("EPI_SHEET_ID", "OOPS")
        
    
    
    doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>
    
    #The specified named sheet of you Google Sheets Worksheet is returned
    sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

    return sheet
   