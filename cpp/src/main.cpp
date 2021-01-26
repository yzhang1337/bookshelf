#include <iostream>

#include "../include/bookshelf/books.hpp"

void prt(std::string s) { std::cout << s << "\n"; }
void prt(std::vector<std::string> v) {
  for (std::string i : v) {
    prt(i);
  };
}

Library make_library() {
  // setup a simple library object
  Book dune("Dune", "Frank Herbert", "zach");
  Book neuromancer("Neuromancer", "William Gibson", "zach");
  Book n84("1984", "George Orwell", "yilun");
  Book candid("Candide", "Voltaire", "yilun");
  Shelf yilun{"yilun"};
  Shelf zach{"zach"};
  zach.add_book(dune);
  zach.add_book(neuromancer);
  yilun.add_book(n84);
  yilun.add_book(candid);
  std::vector<Shelf> shelves{zach, yilun};
  Library library{1};
  library.add_shelf(zach);
  library.add_shelf(yilun);
  return library;
}

std::vector<std::string> list_all_books(const std::vector<Shelf> &shelves) {
  std::vector<std::string> book_names;
  for (Shelf i : shelves) {
    std::vector<std::string> t(i.get_titles());
    book_names.insert(book_names.end(), t.begin(), t.end());
  };
  return book_names;
}

std::string shelf_string(Shelf s) {
  // Create a string of the shelf and all books
  std::string shelf_desc = s.get_owner() + ": ";
  for (std::string title : s.get_titles()) {
    shelf_desc += (title + " ");
  }
  return shelf_desc;
}

std::string show_library(Library lib) {
  // a formatted string showing the library
  std::string lib_string = "Library: \n";
  for (auto i : lib.get_shelfmap()) {
    lib_string += "Shelf " + shelf_string(i.second) + "\n";
  };
  return lib_string;
}

int process_borrow_request() { return 0; }

int main() {
  Library library = make_library();
  prt("All books: ");
  prt(show_library(library));
  log("trasfer dune!");
  LoanNote dune_transfer("Dune", "zach", "yilun");
  library.process_transfer(dune_transfer);
  prt("");
  prt(show_library(library));

  // transfer 1984
  LoanNote n84_transfer("1984", "yilun", "zach");
  library.process_transfer(n84_transfer);
  prt("");
  prt(show_library(library));
}
