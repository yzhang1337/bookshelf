import bookshelf

print("Bookshelf Testing")


# Create some books
dune = bookshelf.Book("Dune", "Frank Herbert")

neuromancer = bookshelf.Book("Neuromancer", "William Gibson")

print(neuromancer.title)

# Create a bookshelf object called zach_shelf
zach_shelf = bookshelf.Shelf('already_read', "availible")

# Add books to the shelf
zach_shelf.add_book(dune)
zach_shelf.add_book(neuromancer)

zach_shelf.print_books()