# app/order_service.py

from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from app.spreadsheet import get_spreadsheet


def restaurant_id(items_list,restaurant_item_list):
    """
    Depending on the items submitted in the website, this function matches the first item's name to its
    respective restaurant. 

    Params: items_list(dictionary), restaurant_item_list(list) 

    Example: restaurant_id('item_dict':[{'name': 'Chicken Sandwhich'}], ["Chicken Sandwhich", "Milkshake", "Waffle Fries"])

    """
    if items_list['item_dict'][0]['name'] in str(restaurant_item_list):
        return True 
    else:
        return False


def UserInfoToSheet(user_info,newSheet):
    """
    Adds a customer's purchase information to a designated output google sheet datastore

    Params: user_info(dictionary), newSheet(gspread Worksheet)
    
    """
    next_row=[]
    num_rows = len(newSheet.get_all_records())+1

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
    """
    Calculates subtotal of a list of products by adding together the price of each individual item
    
    Param: item_selections (list) 
    
    Example: 
    item_selections=[{'name': 'item1', 'price': 2.56}, {'name': 'item2', 'price': 4.52}]
    subtotal_calc(item_selections)
    
    Returns: 7.08
    """
    subtotal = 0
    for item in item_selections:
        subtotal = subtotal + float(item["price"])
    return subtotal


def choices_converter(choice_dict): 

    """
    Converts an unformatted dictionary into a properly formatted list of dictionaries
    
    Param: choice_dict (dictionary) 
    
    Example: choices_converter({'specific name': 'specific value', 'different name': 'different value'})
    
    Returns: [
        {'name': 'specific name', 'price': 'specific value}, 
        {'name': 'different value', 'price': 'different value'}
        ]
    """

    converted_list = []
    for choice in choice_dict:
        next_row={
            'name': choice,
            'price': choice_dict[choice]
        }
        converted_list.append(next_row)
    return converted_list


#This list represents the various restaurant options on the website. 
restaurant_list =[   
    {'id': 1, 'name': "Epicurean"}, 
    {'id': 2, 'name': "CFA"}, 
    {'id': 3, 'name': "Wisey's"},
    {'id': 4, 'name': "Starbucks"}
    ]

#This is populated with orders in the home routes create_user() function
orders_list = []

#This gathers all the menu items from each sheet_name in the provided GOOGLE_SHEET_ID env variable
#and is called from the homeroutes index() function.
CFA_items = get_spreadsheet("Chick Fil A").get_all_records()
Wiseys_items = get_spreadsheet("Wisey's").get_all_records()
Starbucks_items = get_spreadsheet("Starbucks").get_all_records()
EPI_items = get_spreadsheet("Epi").get_all_records()



