# Create Account class with acno, customername, balance. 
# Provide methods to deposit, withdraw, and display balance.

class Account:
    def __init__(self, acno, customername, balance=0):
        self.acno = acno
        self.customername = customername
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.acno}, Customer Name: {self.customername}, Balance: {self.balance}")

