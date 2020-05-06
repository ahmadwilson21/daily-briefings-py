
# web_app/routes/home_routes.py

from flask import Blueprint, render_template, flash, redirect, request
from flask import Flask
from app.order_service import restaurant_list, CFA_items, EPI_items,Wiseys_items,Starbucks_items
from app.order_service import subtotal_calc, choices_converter, to_usd, orders_list, UserInfoToSheet, restaurant_id
from app.send_email import sendEmail
from app.spreadsheet import get_spreadsheet
import ast

home_routes = Blueprint("home_routes", __name__)
restaurant = "None"
@home_routes.route("/")
def index():
    #Home Page
    print("VISITED THE HOME PAGE...")
    return render_template("order_page.html", results = restaurant_list)

@home_routes.route("/order/page", methods=["GET", "POST"])
def order_page():
    print("GENERATING A Order FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        selection = dict(request.form)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        selection = dict(request.args)

    
    # returns the appropriate menu item based on which restaurant you selected
    if(selection):
        if(selection["name"] == "CFA"):
            print("selected name is CFA")
            return render_template("order_items.html", results = CFA_items, restaurant = "CFA") #takes me to order_items.html
        elif(selection["name"] == "Wisey's"):
            print("selected name is Wiseys")
            return render_template("order_items.html", results =Wiseys_items, restaurant = "Wisey's") #takes me to order_items.html
        elif(selection["name"] == "Epicurean"):
            print("selected name is Epicurean")
            return render_template("order_items.html", results =EPI_items, restaurant = "Epicurean") #takes me to order_items.html
        elif(selection["name"] == "Starbucks"):
            print("selected name is Starbucks")
            return render_template("order_items.html", results =Starbucks_items, restaurant = "Starbucks") #takes me to order_items.html
    else:
        return render_template("order_page.html",results = restaurant_list)

@home_routes.route("/order/subtotal", methods=["GET", "POST"])
def order_subtotal():
    #Generates your menu subtotal

    print("GENERATING Order subtotal form...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        selection = dict(request.form)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        selection = dict(request.args)


    selection = choices_converter(selection) #'[{"name": 'name', "price": 3.4}]'
    subtotal = subtotal_calc(selection)
    subtotal= to_usd(subtotal)
    
    return render_template("subtotal.html", results = selection, subtotal = subtotal)
@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE...")
    #return "About Me (TODO)"
    return render_template("about.html")


@home_routes.route("/users/create", methods=["POST","GET"]) #responding to post requests
def create_user():
    print("FORM DATA:", dict(request.form)) #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}
    user = dict(request.form)
    orders_list.append(user)
    print(orders_list)
    
    #user[item_dict] is returned as a string of values so this converts it into an accessible list
    user['item_dict'] = ast.literal_eval(user['item_dict'])
    
    #if item is from Starbucks restaurant
    if restaurant_id(user,Starbucks_items):
        newSheet = get_spreadsheet("Starbucks",1)

    #if item is from CFA restaurant 
    elif restaurant_id(user,CFA_items):
        newSheet = get_spreadsheet("Chick Fil A",2)

    #if item is from Wisey's restaurant
    elif restaurant_id(user,Wiseys_items):
        newSheet = get_spreadsheet("Wisey's",3)

    #if item is from Epicurean restaurant
    elif restaurant_id(user,EPI_items):
        newSheet = get_spreadsheet("Epi",4)

    #This adds the items from the request form into the specified google sheet datastore
    UserInfoToSheet(dict(request.form), newSheet)

    #Sends email to the user with their form information
    sendEmail(user['email_address'],user)


    flash(f"User '{user['full_name']}' with email '{user['email_address']}' created successfully!", "success")
    
    return redirect("/")