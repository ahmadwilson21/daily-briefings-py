# final-project/test/order_test.py

from app.order_service import restaurant_id, UserInfoToSheet, to_usd, subtotal_calc, choices_converter

def test_restaurant_id():
    test_item = {'item_dict':[{'name': 'Chicken Sandwich'}]}
    
    test_restaurant_item_list = ['Chicken Sandwich', 'Chicken Nuggets', 'Chocolate Milkshake']

    result = restaurant_id(test_item,test_restaurant_item_list)
    assert result == True

def test_to_usd():
    result = to_usd(1500)
    assert result == "$1,500.00"

    result = to_usd(98.78384)
    assert result == "$98.78"

    result = to_usd(2.5)
    assert result == "$2.50"

def test_subtotal_calc():
    item_list = [
        {"name": "Iced coffee", "price": 3.50},
        {"name": "Iced tea", "price": 2.50},
        {"name": "Caramel Latte", "price": 4.95},
        {"name": "Strawberry Frappuccino", "price": 4.75}
    ]

    result = subtotal_calc(item_list)
    assert result == 15.7

def test_choices_converter():
    test_dict = {'specific name': 'specific value','different name': 'different value'}

    result = choices_converter(test_dict)
    assert result == [
        {'name': 'specific name','price': 'specific value'}, 
        {'name': 'different name','price': 'different value'}
    ]

