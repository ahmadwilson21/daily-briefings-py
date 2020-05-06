
# app/order_service.py


from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from app.spreadsheet import get_spreadsheet
load_dotenv()

# Google Sheets API Keys
DOCUMENT_ID = os.environ.get("GOOGLE_SHEET_ID", "OOPS")
NEW_SHEET_ID = os.environ.get("NEW_SHEET_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "products")

restaurant_list =[{
    'id': 1 ,'name': 'Epicurean'}, 
    
    {'id': 2, 'name': 'CFA'}, 
    {'id': 3, 'name': "Wisey's"},
    {'id': 4, 'name': "Starbucks"}
    ]
def restaurant_id(items_list,restaurant_list):
    print("Entered restaurant id func")
    
    
    if items_list['item_dict'][0]['name'] in str(restaurant_list):
        print("Yes happy ending")
        return True 
    else:
        return False

    
    

CFA_items = get_spreadsheet("Chick Fil A").get_all_records()
Wiseys_items = get_spreadsheet("Wisey's").get_all_records()
Starbucks_items = get_spreadsheet("Starbucks").get_all_records()
EPI_items = get_spreadsheet("Epi").get_all_records()

###REPLACE THESE WITH THE NAMES OF YOUR RESPECTIVE SHEETS, IF NOT USING PROVIDED EXAMPLE GOOGLE SHEET
#Starbucks_Sheet = get_spreadsheet("Starbucks",1)
#CFA_Sheet = get_spreadsheet("CFA",2)
#Wiseys_Sheet = get_spreadsheet("Wisey's",3)
#EPI_Sheet = get_spreadsheet("EPI",4)


restaurant_list =[{
    'id': 1 ,'name': 'Epicurean'}, 
    
    {'id': 2, 'name': 'CFA'}, 
    {'id': 3, 'name': "Wisey's"},
    {'id': 4, 'name': "Starbucks"}
    ]
orders_list = []


def UserInfoToSheet(user_info,newSheet):
    """
    Adds a customers user information to a designated output google sheet datastore
    """
    next_row=[]
    num_rows = len(newSheet.get_all_records())+1
 
    #PRODUCTS_LIST.append(next_row) #adds the new row to product list
    #next_row = list(value_dict.values()) #collects values in order to add to the google sheet
    next_row = list(user_info.values())
    num_rows = num_rows + 1 #the new location of the object is the last row position + 1
    newSheet.insert_row(next_row, num_rows) #inserts new row into sheet

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71
def subtotal_calc(item_selections):
    subtotal = 0
    for item in item_selections:
        subtotal = subtotal + float(item["price"])
    return subtotal

def choices_converter(choice_dict): 
    #converts a dictionary with attributes {'specific name': 'specific value','specific name': 'specific value'} to 
    #a list [{'name': 'specific name','value': 'specific value'}, {'name': 'specific name', 'value': 'specific value'}]
    
    converted_list = []
    for choice in choice_dict:
        next_row={
            'name': choice,
            'price': choice_dict[choice] 

        }
        converted_list.append(next_row)
    return converted_list