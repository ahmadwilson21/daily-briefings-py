
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


CFA_items = get_spreadsheet("Chick Fil A",0).get_all_records()
Wiseys_items = get_spreadsheet("Wisey's",0).get_all_records()
Starbucks_items = get_spreadsheet("Starbucks",0).get_all_records()
EPI_items = get_spreadsheet("Epi",0).get_all_records()

newSheet = get_spreadsheet("Epi",2)
num_rows = len(newSheet.get_all_records())
restaurant_list =[{
    'id': 1 ,'name': 'Epicurean'}, 
    
    {'id': 2, 'name': 'CFA'}, 
    {'id': 3, 'name': "Wisey's"},
    {'id': 4, 'name': "Starbucks"}
    ]
orders_list = []



def getValues(value_dict,newSheet):
    next_row=[]
    num_rows = len(newSheet.get_all_records())+1
   # next_row = {
   #             
#
   #             'name': name, 
   #             'price': price,
   #             
   #             }
    #PRODUCTS_LIST.append(next_row) #adds the new row to product list
    next_row = list(value_dict.values()) #collects values in order to add to the google sheet
    num_rows = num_rows + 1 #the new location of the object is the last row position + 1
    newSheet.insert_row(next_row, num_rows) #inserts new row into sheet




#CFA_items =[
#    {'id': 1, 'name': 'CFA-Sandwhich', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 2, 'name': 'Meal-CFA-Sandwhich', 'category': 'sandwhich', 'price': 5.95},
#    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
#    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
#    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
#    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
#    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
#    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
#    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
#    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
#    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05},
#    {'id': 1, 'name': 'CFA Sandwhich', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 2, 'name': 'Meal CFA Sandwhich', 'category': 'sandwhich', 'price': 5.95},
#    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
#    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
#    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
#    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
#    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
#    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
#    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
#    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
#    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05},
#    {'id': 1, 'name': 'CFA Sandwhich', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 2, 'name': 'Meal CFA Sandwhich', 'category': 'sandwhich', 'price': 5.95},
#    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
#    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
#    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
#    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
#    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
#    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
#    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
#    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
#    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
#    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05}
#]
#
#Starbucks_items = [
#    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
#    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
#    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95}
#]
#
#EPI_items= [
#    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
#    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
#    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05}
#]
#
#Wiseys_items = [
#    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
#    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
#    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05}
#]
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
    #a list [{'name': 'specific name'}, {'value': 'specific value'}, {'name': 'specific name'}, {'value': 'specific value'}]
    converted_list = []
    for choice in choice_dict:
        next_row={
            'name': choice,
            'price': choice_dict[choice] 

        }
        converted_list.append(next_row)
    return converted_list