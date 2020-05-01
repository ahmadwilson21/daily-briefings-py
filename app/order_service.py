
# app/order_service.py


from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

# Google Sheets API Keys
DOCUMENT_ID = os.enviroxn.get("GOOGLE_SHEET_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "products")





restaurant_list =[{
    'id': 1 ,'name': 'Epicurean'}, 
    
    {'id': 2, 'name': 'CFA'}, 
    {'id': 3, 'name': "Wisey's"},
    {'id': 4, 'name': "Starbucks"}
    ]
orders_list = []



    


CFA_items =[
    {'id': 1, 'name': 'CFA-Sandwhich', 'category': 'sandwhich', 'price': 3.05},
    {'id': 2, 'name': 'Meal-CFA-Sandwhich', 'category': 'sandwhich', 'price': 5.95},
    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05},
    {'id': 1, 'name': 'CFA Sandwhich', 'category': 'sandwhich', 'price': 3.05},
    {'id': 2, 'name': 'Meal CFA Sandwhich', 'category': 'sandwhich', 'price': 5.95},
    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05},
    {'id': 1, 'name': 'CFA Sandwhich', 'category': 'sandwhich', 'price': 3.05},
    {'id': 2, 'name': 'Meal CFA Sandwhich', 'category': 'sandwhich', 'price': 5.95},
    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05},
    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95},
    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05},
    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05}
]

Starbucks_items = [
    {'id': 1, 'name': 'Cafe Mocha', 'category': 'Coffee', 'price': 3.65},
    {'id': 2, 'name': 'Iced Coffee', 'category': 'Coffee', 'price': 2.65},
    {'id': 3, 'name': 'Coffee Frappuccino', 'category': 'Frappuccino', 'price': 3.95}
]

EPI_items= [
    {'id': 1, 'name': 'Mrs.Reuben', 'category': 'Sandwhich', 'price': 7.25},
    {'id': 2, 'name': 'Epi Chicken Quesadilla', 'category': 'Quesadilla', 'price': 7.45},
    {'id': 3, 'name': 'Epi Veggie Burrito', 'category': 'Burrito', 'price': 3.05}
]

Wiseys_items = [
    {'id': 1, 'name': 'Chicken Madness', 'category': 'Best Seller', 'price': 7.25},
    {'id': 2, 'name': 'Burger Madness', 'category': 'Best Seller', 'price': 7.45},
    {'id': 3, 'name': 'Quarter Pound Burger', 'category': 'Burger', 'price': 3.05}
]
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