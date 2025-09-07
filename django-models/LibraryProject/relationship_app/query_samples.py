#query all books for a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

#list all books in a library
library = Library.objects.get(name="KPL")
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

#retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")