"""Mini Project using methods and OOPS
"""

class User:
    def __init__(self, name, email, account_pin):
        self.name = name                      # Public
        self._email = email                   # Protected
        self.__account_pin = account_pin      # Private

    def display_user_info(self):
        return f"User: {self.name}, Email: {self._email}"

    def __verify_pin(self, pin):
        return pin == self.__account_pin      # Private method

    def authenticate(self, pin):
        if self.__verify_pin(pin):
            return "Access granted"
        else:
            return "Access denied"


class BankAccount(User):
    def __init__(self, name, email, account_pin, balance):
        super().__init__(name, email, account_pin)
        self._balance = balance               # Protected

    def show_balance(self):
        return f"{self.name}'s balance is ₹{self._balance}"  # Public method

    def _deduct_balance(self, amount):       # Protected method
        if amount <= self._balance:
            self._balance -= amount
            return f"₹{amount} deducted. New balance: ₹{self._balance}"
        else:
            return "Insufficient funds"

    def withdraw(self, amount, pin):
        if self.authenticate(pin) == "Access granted":
            return self._deduct_balance(amount)
        else:
            return "Authentication failed"


class LoanAccount(BankAccount):
    def __init__(self, name, email, account_pin, balance, loan_limit):
        super().__init__(name, email, account_pin, balance)
        self.loan_limit = loan_limit

    def apply_loan(self, amount):
        if amount <= self.loan_limit:
            self._balance += amount
            return f"Loan of ₹{amount} approved. New balance: ₹{self._balance}"
        else:
            return f"Loan request exceeds limit of ₹{self.loan_limit}"


customer = LoanAccount("Aniruddhan", "aniruddhan@example.com", 1234, 10000, 50000)


print(customer.display_user_info())            
print(customer.show_balance())                   


print(customer.withdraw(5000, 1234))             
print(customer.withdraw(2000, 1111))             


print(customer.apply_loan(30000))                
print(customer.apply_loan(60000))                


try:
    print(customer.__account_pin)                
except AttributeError as e:
    print("Private access error:", e)

# ✅ Name mangling way (not recommended)
print("Accessing private attribute via mangling:", customer._User__account_pin)
