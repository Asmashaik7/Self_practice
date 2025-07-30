# 🔹 Next Task – Mini Project
# 👉 Create a Library System class with:
# Add book → Takes title and author, adds to a list
# Show all books → Prints all books in the library
# Remove a book → Removes a book by title

class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self,title,author):
        self.books.append({'title': title, 'author': author})

    def show_books(self):
            if self.books:
                for book in self.books:
                    print(f"{book['title']} by {book['author']}")
            else:
                print("No books in the library.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"Removed '{title}' from library")
                return
        print(f"Book '{title}' not found.")

# Using the class
lib = Library()
lib.add_book("Python Basics", "John")
lib.add_book("SQL Guide", "Alice")
lib.show_books()
lib.remove_book("Python Basics")
lib.show_books()
