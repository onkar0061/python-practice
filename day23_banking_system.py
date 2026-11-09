from abc import ABC, abstractmethod


class BankAccountTemplate(ABC):
    @abstractmethod
    def account_type(self):
        pass


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

        else:
            print("Invalid Amount")

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance = self.__balance - amount
        elif amount > self.__balance:
            print("Insufficient Funds ")
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount, BankAccountTemplate):
    def account_type(self):
        print("Account Type: Saving Account")

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def show_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.interest = interest
        print(f"interest Rate:{self.interest}")


class CurrentAccount(BankAccount, BankAccountTemplate):
    def account_type(self):
        print("Account Type: Current Account")

    def __init__(self, name, balance):
        super().__init__(name, balance)


c1 = CurrentAccount("Onkar",10000)
s1 = SavingAccount("Onkar", 5000, 5)
s1.deposit(1000)
s1.withdraw(500)
accounts = [s1, c1]
for account in accounts:
    account.account_type()
    print(f"Account Balance: {account.get_balance()}")
s1.show_interest()
