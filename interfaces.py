# Document 1 use case of an interface in python
# That is define an interface using the abstract base class module
# Add at least 3 entities that can implement the interface in a way that make sense.

from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, owner, interest_rate):
        self.owner = owner
        self.interest_rate = interest_rate
        self.balance = 0

    @abstractmethod
    def deposit(self, amount):
        self.balance += amount
        print("Your account has been credited. New Balance: %.2f" %self.balance)

    @abstractmethod
    def withdraw(self, amount):
        self.balance -= amount
        print("Your account has been debited. New Balance: %.2f" %self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate):
        super().__init__(owner, interest_rate)
        self.interest_rate = 0.06

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if self.balance - amount > 0:
            super().withdraw(amount)
        else:
            print("Insufficient funds")
    

class CurrentAccount(BankAccount):
    
    def __init__(self, owner, interest_rate):
        super.__init__(owner, interest_rate)
        self.interest_rate = 0

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if self.balance - amount > 1000:
            super().withdraw(amount)
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

class LotteryAccount(BankAccount):
    
    def __init__(self, owner, interest_rate):
        super().__init__(owner, interest_rate)
        self.interest_rate = 0

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        super().withdraw(amount)

a = SavingsAccount('Sayo', 0.06)
print(a.interest_rate)
print(a.owner)
print(a.balance)
print(a.deposit(2000))
print(a.deposit(2000))
print(a.withdraw(520))
