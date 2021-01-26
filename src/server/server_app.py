import json
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# This is a very simple web server!
# Each website page is called a "route". The functions on the server
# get called when you go to the page listed on the route.

# You can get data or send data to the server with the different http GET/POST
# commands. This server does not show any html pages, so it responds to manual
# http requests. These can be made using the python "requests" library.


# This server isn't setup to use the actuall bookshelf code yet, it's just a
# basic stand-in or framework for us to fill in.

@app.route('/', methods=['GET'])
def home():
    return (
        "<h1>BOOKSHELF</h1><p> Your own, distributed library!</p>"
    )


@app.route('/register', methods=['POST'])
def register():
    # Add a new user to the user_data dictionary

    # Get the user and password from the request data that we sent. Data is
    # stored in the "form" variable.
    user = request.form['user']
    passwd = request.form['password']

    if user in user_data:
        return "User already exists"

    # Create the user in the user_data dictionary.
    user_data[user] = {
        "password": passwd,
        "book_list": [],
        "friends": []  # list of friends
    }
    print("User added: ", user)
    return f"User {user} added!"


@app.route('/books/<user>', methods=['GET', 'POST'])
def books(user):
    # This function can be called with a get or post.
    # GET returns the list of books for the given user.

    if request.method == 'GET':
        return json.dumps(user_data[user]["book_list"])
    if request.method == 'POST':
        book_to_add = request.form['book']
        user_data[user]["book_list"].append(book_to_add)
        return "book added"


# Dict of users, with password and bookshelf info
user_data = {}

# This starts the server. The other functions are called when a request is
# recieved.
app.run()
