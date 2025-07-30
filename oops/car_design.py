#  Question 1 – Create a Car Class with Attributes
# 👉 Task:
# Create a class Car
# It should have two attributes: brand and model
# Create two objects of this class and print their details

class car:
    def __init__(self,brand,model): #init is a constructor used to initialize the object of the class, self is the current object
        self.brand=brand
        self.model=model

car1=car('Tata','Tiago')
car2=car('Maruti','Alto')
car3=car('Hyundai','Creta')

print(car1.brand, car1.model)
print(car2.brand, car2.model)
print(car3.brand, car3.model)

# 📌 Key Points in Your Code
# 1️⃣ class car: → Defines a class (blueprint).
# 2️⃣ __init__ → Constructor, runs automatically when an object is created.
# 3️⃣ self.brand = brand → Saves data inside the current object.
# 4️⃣ car1, car2, car3 → Objects (instances) created from the car class.