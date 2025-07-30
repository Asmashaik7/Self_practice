# # Dunder (Magic) Methods in Python  


# ✅ Example:
 
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} has {self.pages} pages"

    def __len__(self):
        return self.pages

book1 = Book("Python Basics", 300)
print(book1)        # Python Basics has 300 pages
print(len(book1))   # 300


# Without _str_, print(book1) shows something like <_main_.Book object at 0x...>  
# Without _len_, len(book1) raises an error.

