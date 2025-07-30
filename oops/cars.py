# Question 2 – Add a Method to Print Car Details
# 👉 Task:
# Add a method car_info() inside the class.
# Instead of printing details outside, call car_info() for each object

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def car_info(self):# include self as the first parameter, else error will be generated
        print(f"Brand: {self.brand}, Model: {self.model}")

car1 = Car("Tata", "Tiago")
car2 = Car("Maruti", "Alto")
car3 = Car("Hyundai", "Creta")

car1.car_info()
car2.car_info()
car3.car_info() 

# Why Error Happened?
# Because in Python, the first parameter of every instance method must be self (to refer to the current object).
# Without it, Python doesn’t know which object’s brand and model to access.
# self must be included in every instance method.
# ✔ It refers to the object that is calling the method.
