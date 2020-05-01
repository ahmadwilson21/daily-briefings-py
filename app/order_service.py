
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
    {'id': 3, 'name': "Wisey's"}




    
]

CFA_items =[
    {'id': 1, 'name': 'CFA Sandwhich', 'category': 'sandwhich', 'price': 3.05},
    {'id': 2, 'name': 'Meal CFA Sandwhich', 'category': 'sandwhich', 'price': 5.95},
    {'id': 3, 'name': 'Milkshake', 'category': 'sandwhich', 'price': 3.05}

]

EPI_items = []


def subtotal_calc(item_selections, restaurant_items):
    subtotal = 0
    for selection in item_selections:
        for item in restaurant_items:
            if selection == item['name']:
                subtotal = subtotal + item['price']
    return subtotal