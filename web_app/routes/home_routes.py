
# web_app/routes/home_routes.py

from flask import Blueprint, render_template, flash, redirect, request
from flask import Flask, url_for
from app.order_service import restaurant_list, CFA_items, EPI_items,Wiseys_items,Starbucks_items, subtotal_calc, choices_converter, to_usd, orders_list
from app.send_email import sendEmail

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE...")
    #return "Welcome Home (TODO)"
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

    
    print(CFA_items)
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

#@home_routes.route("/order/select", methods=["GET", "POST"])
#def order_select():
#    print("GENERATING Order selection form...")
#
#    if request.method == "POST":
#        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
#        selection = dict(request.form)
#    elif request.method == "GET":
#        print("URL PARAMS:", dict(request.args))
#        selection = dict(request.args)
#
#    print(selection)
#    
#    return render_template("subtotal.html", results = CFA_items, restauraunt = 'CFA')

@home_routes.route("/order/subtotal", methods=["GET", "POST"])
def order_subtotal():
    print("GENERATING Order subtotal form...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        selection = dict(request.form)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        selection = dict(request.args)

    selection = choices_converter(selection) #'[{"name": 'name', "price": 3.4}]'
    subtotal = subtotal_calc(selection)
    print("entered subtotal homeroute")
    print(to_usd(subtotal))
    subtotal= to_usd(subtotal)
    
    return render_template("subtotal.html", results = selection, subtotal = subtotal)
@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE...")
    #return "About Me (TODO)"
    return render_template("about.html")

@home_routes.route("/users/new")
def new_user():
    print("VISITED THE NEW USER REGISTRATION PAGE...")
    #return "Sign Up for our Product! (TODO)"
    return render_template("new_user_form.html")

@home_routes.route("/users/create", methods=["POST","GET"]) #responding to post requests
def create_user():
    #print("RECIEVED FROM INPUTS")
    print("FORM DATA:", dict(request.form)) #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}
    user = dict(request.form)
    orders_list.append(user)
    print(orders_list)
    sendEmail(user['email_address'],user)
    # todo: store in a database or google sheet! ADD This person to a google sheet datastore
    flash(f"User '{user['full_name']}' with email '{user['email_address']}' created successfully!", "danger")
    #flash(f"User '{user['full_name']}' created successfully! (TODO)", "warning")
    return redirect("/")