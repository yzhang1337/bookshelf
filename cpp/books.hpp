#include <iostream>
#include <map>
#include <string>
#include <vector>

void log(std::string info) { std::cout << "[INFO] " << info << "\n"; }

class LoanNote {
public:
  bool on_loan;
  std::string owner;
  std::string loan_date;
  std::string loaned_to;
  std::string book_name;

  LoanNote(std::string book, std::string own, std::string to);
  std::string from() { return owner; }
  std::string to() { return loaned_to; }
  std::string title() { return book_name; }
};

LoanNote::LoanNote(std::string book, std::string own, std::string to) {
  book_name = book;
  owner = own;
  loaned_to = to;
  loan_date = "today";
}

class Book {
  std::string title, author, owner;
  bool available;

public:
  Book(std::string t, std::string a, std::string o)
      : title(t), author(a), owner(o), available(false) {}
  std::string get_author() { return author; }
  std::string get_title() { return title; }
  std::string get_owner() { return owner; }
  bool is_available() { return available; }
};

class Shelf {
  std::vector<Book> books;
  std::vector<Book> loaned_books;
  std::string owner;

public:
  Shelf() : owner("none") {}
  Shelf(std::string o) : owner(o) {}
  std::vector<Book> get_books() { return books; }
  std::vector<Book> list_loaned() { return loaned_books; }
  void add_book(Book b) { books.push_back(b); }
  std::string get_owner() { return owner; }
  std::vector<std::string> get_titles();
  Book get_loan(const std::string &title);
};

std::vector<std::string> Shelf::get_titles() {
  std::vector<std::string> titles;
  for (Book i : books) {
    titles.push_back(i.get_title());
  };
  return titles;
}

Book Shelf::get_loan(const std::string &title) {
  // return the book to be loaned, move it to the loaned_books
  int book_loc;
  bool book_found = false;
  log(owner + ": getting loan from shelf: " + title);
  for (int i = 0; !book_found && (i < books.size()); i++) {
    log("checking book title");
    if (books[i].get_title() == title) {
      book_loc = i;
      log("found book: " + title);
      book_found = true;
    };
  };
  log("pulling book");
  Book loaned_book = books[book_loc];
  loaned_books.push_back(loaned_book);
  books.erase(books.begin() + book_loc);
  log("giving loan up");
  return loaned_book;
}

class Library {
  std::map<std::string, Shelf> shelf_map;
  std::vector<LoanNote> current_loans;
  int id;

public:
  Library(int i) : id(i) {}
  void add_shelf(Shelf shelf);
  void process_transfer(LoanNote request);
  void process_return(std::string title, std::string owner);
  int get_id() { return id; }
  std::map<std::string, Shelf> get_shelfmap() { return shelf_map; }
};

void Library::add_shelf(Shelf shelf) {
  shelf_map[shelf.get_owner()] = Shelf(shelf);
}

void Library::process_transfer(LoanNote request) {
  // get the book from the transfer request
  log("starting transfer process");
  Book transfer = shelf_map[request.from()].get_loan(request.title());
  log("got book " + transfer.get_title());
  log("adding book to shelf: " + request.to());
  shelf_map[request.to()].add_book(transfer);
  log("Recording the loan");
  current_loans.push_back(request);
}

void Library::process_return(std::string title, std::string owner) {
  // TODO
}
