import requests

# The website URL when the server is running locally.
url = "http://localhost:5000/"


resp = requests.get(url)
print(resp.text)


# These functions take in parameters, and use them to call the intended
# http request on the server. Ther server comes back with a response object.
def register_user(name, passwd):
    # Add a user to the server

    func_url = url + "register"
    # Package the username and password into a dictionary, to send to the
    # server.
    login = {"user": name, "password": passwd}
    resp = requests.post(func_url, data=login)
    print(resp.text)


def get_books(user):
    # Get the list of existing books for this user.
    func_url = url + "books/" + user
    resp = requests.get(func_url)
    print(resp.json())
    return resp.json()


def add_book(user, title):
    # Add a book to this user's book list.
    func_url = url + "books/" + user
    book_data = {"book": title}
    resp = requests.post(func_url, data=book_data)
    print(resp.text)
    return resp.text


if __name__ == "__main__":
    # This gets run when you run it as a script. If you import this file it
    # this does not run.

    user = 'zach'
    pw = 'zachisthebest'
    register_user(user, pw)

    book = {"book": "Dune"}
    resp = requests.post(url+"books/"+user, data=book)
    print(resp.text)

    print(requests.get(url+"books/zach").json())
