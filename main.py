'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class BankAccount:
    bank_name = "Global Bank"  # Class variable

    def __init__(self, acc_holder, balance=100):
        self.acc_holder = acc_holder  # Instance variable
        self.balance = balance        # Instance variable

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def display(self):
        return f"Account Holder: {self.acc_holder}, Bank: {BankAccount.bank_name}, Balance: {self.balance}"

# Creating instances
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

# Accessing class and instance variables
print(acc1.deposit(200))
print(acc1.display())
print(acc2.display())
print(acc2.deposit(300))

# Change class variable
BankAccount.bank_name = "Universal Bank"

print(acc2.display())
print(acc2.deposit(300))

print(acc1.display())  # Reflects updated class variable
print(acc2.display())

