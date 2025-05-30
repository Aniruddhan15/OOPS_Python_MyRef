print("Try programiz.pro")

class Bank:
    def __init__(self, name, accountno, ifsc):
        self.name = name
        self._accountno = accountno         # Protected
        self.__ifsc = ifsc                  # Private
        self.balance = 0                    # Add balance to base class

    def show_balance(self):
        return f"Balance: ₹{self.balance} for IFSC: {self.__ifsc}, Name: {self.name}"


class Withdraw(Bank):
    def __init__(self, name, accountno, ifsc, balance):
        super().__init__(name, accountno, ifsc)
        self.balance = balance  # Properly set balance in subclass too

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient balance for {self._accountno}"
        else:
            self.balance -= amount
            return f"₹{amount} withdrawn. New balance: ₹{self.balance}"

    def deposit(self, money):
        self.balance += money
        return f"₹{money} deposited. New balance for account {self._accountno}: ₹{self.balance}"


# Driver code
acc = Withdraw("Aniruddhan", 10001, "IDIB0001234", 10000)
print(acc.deposit(5000))
print(acc.withdraw(4000))
print(acc.withdraw(15000))
print(acc.show_balance())
