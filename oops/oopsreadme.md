Class
A class is like a blueprint for creating objects.
It defines properties (attributes) and behaviors (methods).

Object
An object is an instance of a class.
When you create an object, it has its own data but follows the structure of the class.


class Student:
    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable

student1 = Student("Asha", 85)
student2 = Student("Ravi", 92)

print(student1.name, student1.marks)
print(student2.name, student2.marks)
📌 Explanation
✅ Class → Student (Blueprint for creating students)
✅ Objects → student1 and student2 (two students created from class)
✅ Attributes → name, marks (unique data for each object)

🔹 Built-in Objects
Python already has predefined classes.

x = 10          # x is object of class int
y = "Hello"     # y is object of class str
z = [1, 2, 3]   # z is object of class list
Here:

int, str, list → built-in classes
x, y, z → built-in objects

🔹 What is self?
self represents the current object. It allows each object to store its own data.

Example:

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Asha")
s2 = Student("Ravi")

print(s1.name)  # Asha
print(s2.name)  # Ravi
👉 Without self, Python would not know which object’s data you are referring to.
It is just a naming convention for the first parameter in any instance method of a class.

📌 What Actually Happens?
When you write:

class Student:
    def __init__(self, name):
        self.name = name
and create an object:

s1 = Student("Asha")
Python automatically calls:

Student.__init__(s1, "Asha")
👉 Here, s1 is passed as the first argument → stored as self.

🔹 Important Points
✅ self refers to the current object.
✅ It can be named anything (like this, obj), but by convention we always use self.

Example:

class Student:
    def __init__(object, name):
        object.name = name

s1 = Student("Asha")
print(s1.name)  # Works fine even if we wrote "object" instead of "self"
So, self is not a keyword, not a variable – just the first parameter representing the current object.



✅Common Interview Questions
What is the difference between class and object?

What is the use of __init__ method?

What are dunder methods (like __str__, __len__)?

What is the difference between class variables and instance variables?

Explain inheritance, polymorphism, encapsulation, abstraction in Python.

Can you create a small class to represent something (like Employee, Car, Book)?

✅ 1. Quick OOP Cheat Sheet
🔹 Class → Blueprint for objects.
🔹 Object → Instance of a class.
🔹 __init__() → Constructor (runs automatically when object is created).
🔹 self → Refers to the current object.
🔹 Instance Variables → Belong to each object.
🔹 Class Variables → Shared by all objects of that class.
🔹 Dunder Methods → Special methods like __str__, __len__, __add__, etc.
🔹 OOP Pillars → Inheritance, Polymorphism, Encapsulation, Abstraction.




