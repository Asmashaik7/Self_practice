# 🔹 Task – Bank Account Class (Small)
# 👉 Create a class BankAccount with:
# ✅ __init__ → to store name and balance
# ✅ deposit(amount) → adds amount to balance
# ✅ show_balance() → prints current balance

class bank_account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
    
    def show_balance(self):
        print(f"{self.name} balance: {self.balance}")

    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")

obj1=bank_account('Asma',3000)
obj1.show_balance()
obj2=bank_account('Ayman',5000)
obj2.show_balance()
obj3=bank_account('zoya',10000)
obj3.show_balance()
obj2.deposit(20000)
obj2.show_balance()

obj2.show_balance()
obj2.withdraw(2000) #withdrawals
obj2.show_balance()

obj1.withdraw(3500)
obj1.show_balance()



#  🔹 Next Step (Optional Improvement)
# Add a withdraw() method with a condition: done  
