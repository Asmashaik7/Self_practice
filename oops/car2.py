# 🔹 Question 3 – Add __str__ Method
# 👉 Task:
# Add __str__ inside the class.
# When you print(car1), it should directly show brand and model.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
    
    def __str__(self):  # special method
        return f"Brand: {self.brand}, Model: {self.model}"
    
    def __len__(self):
        return len(self.model)

car1 = Car("Tata", "Tiago")
car2 = Car("Maruti", "Alto")
car3 = Car("Hyundai","Creta")

print(car1)   # Uses __str__ automatically, here car1, car2, car3 are objects of car, when we print objects actually errors comes , by using __str__ it shows human readable format of object.
print(car2)
print(car3)

print(len(car1))
print(len(car2))
print(len(car3))


# ✅ __str__ is a special (dunder) method in Python.
# 👉 So __str__ gives a human-readable description of the object.
# Officially → Special method __str__
# Purpose → Returns a string representation of the object
# This is very useful in interviews & real-world projects, because it makes debugging and printing objects much easier.

# 📌 Purpose of __str__
# It controls what gets displayed when you use print(object) or str(object).

# Without __str__, printing an object shows something like:<__main__.Car object at 0x00000234ABCDEF>


# ✅ Python calls len(object) → internally runs object.__len__()
# ✅ If __len__ is not defined → TypeError: object of type 'Car' has no len()
# For built-in classes (str, list, dict, etc.), Python already has __len__ defined inside them.
# For your custom class, Python has no idea what "length" means.
# 👉 So, you define __len__ to tell Python how to calculate the length for that object.