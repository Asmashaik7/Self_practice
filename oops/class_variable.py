# 🔹 Next Task – Question 5
# 👉 Add a Class Variable
# 📌 What is a Class Variable?
# A variable shared by all objects of a class.
# Defined inside the class but outside methods.
# Accessed using ClassName.variable or self.variable.

# 📝 Task:
# Add a class variable vehicle_type = "Car" inside the class.
# Print it using both object and class name.

class Car:
    vehicle_type="car" # ✅ Class variable (shared by all objects)vehicle_type is same for all cars, so it is a class variable.brand and model are instance variables (different for each object).

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

# Accessing class variable
print(Car.vehicle_type) #using class name is correct method
print(car1.vehicle_type) #can use by using object, but not recommended


print(car1)   # Uses __str__ automatically, here car1, car2, car3 are objects of car, when we print objects actually errors comes , by using __str__ it shows human readable format of object.
print(car2)
print(car3)

print(len(car1))
print(len(car2))
print(len(car3))
