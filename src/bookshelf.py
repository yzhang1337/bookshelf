from datetime import date
# for getting dates


class Shelf():
    def __init__(self, shelf_type):
        """
        param shelf_type: boolean
        """
        self.shelf_type = shelf_type
        self.books = [] # Empty list to start out
    
    def add_book(self, book):
        # Adds a book object to this shelf
        self.books.append(book)
        print("Added book to shelf: ", book.title)

        ## Potentially add date and time?
    
    def print_books(self):
        # prints all of the book titles on this shelf
        for book in self.books:
            print(book.title)
    
    def remove_book(self, book):
        
        self.print_books()
        self.books.remove(book)
        print("removed: ", book.title)


class Library():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.build_shelves()

    def build_shelves(self):
        self.shelf_type = ['Available','Currently Reading','Wishlist','Holding']
        self.Available = Shelf(self.shelf_type[0])
        self.Current = Shelf(self.shelf_type[1])
        self.Wishlist = Shelf(self.shelf_type[2])
        self.Holding = Shelf(self.shelf_type[3])
    
    
    def add_user(self, name):
        print("Welcome to your library ", first_name, "!")

    def shelf_summary(self):

        for shelf_type in self.shelf_type:
            print(shelf_type)
            shelf.print_books(shelf_type)


class Book():
    """
    A Class representing a single book

    (this is a docstring, to document how the class works)
    """
    
    def __init__(self, title, author, genre):
        # The __init__ function gets called when an instance of a class
        # is created. It runs any setup code, and creates class variables.
        
        # This is an instance variable, created for every book object
        # The "self." means that this variable is specific to the instance of the class
        self.title = title
        self.author = author
        genre = []
    def get_shelf_life()
        # for getting 
    