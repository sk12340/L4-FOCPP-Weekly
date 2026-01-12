class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        except ValueError as e:
            print("Error:", e)
    
    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(200)
acc.withdraw(30)
print(f"Final balance: {acc.get_balance()}")