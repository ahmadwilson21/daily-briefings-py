
# web_app/routes/home_routes.py

from flask import Blueprint, render_template, flash, redirect, request
from app.order_service import restaurant_list, CFA_items, EPI_items, subtotal_calc

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

    
    print(selection["name"])

    if(selection["name"] == "CFA"):
        print("selected name is CFA")
        return render_template("order_items.html", results = CFA_items, restaurant = "CFA") #takes me to order_items.html
    else:
        return render_template("order_items.html")

@home_routes.route("/order/select", methods=["GET", "POST"])
def order_select():
    print("GENERATING Order selection form...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        selection = dict(request.form)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        selection = dict(request.args)

    print(selection)
    
    return render_template("subtotal.html", results = CFA_items, restauraunt = 'CFA')

@home_routes.route("/order/subtotal", methods=["GET", "POST"])
def order_subtotal():
    print("GENERATING Order selection form...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        selection = dict(request.form)
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        selection = dict(request.args)

    
    
    return render_template("subtotal.html", results = CFA_items, restauraunt = 'CFA')
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

@home_routes.route("/users/create", methods=["POST"]) #responding to post requests
def create_user():
    #print("RECIEVED FROM INPUTS")
    print("FORM DATA:", dict(request.form)) #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}
    user = dict(request.form)
    # todo: store in a database or google sheet! ADD This person to a google sheet datastore
    flash(f"User '{user['full_name']}' created successfully!", "danger")
    #flash(f"User '{user['full_name']}' created successfully! (TODO)", "warning")
    return redirect("/")