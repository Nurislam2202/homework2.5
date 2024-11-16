class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, overdraft_limit, balance=0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def list_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Owner: {account.owner}, Balance: {account.balance}")

    def total_funds(self):
        total = sum(account.get_balance() for account in self.accounts)
        print(f"Total funds in the bank: {total}")
        return total


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, interest_rate, balance=0):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self, amount):
        if amount < 0 or amount > 100:
            print('enter numbers only from 0 to 100')
        elif amount == 0:
            print(f'balance: {self.balance}')
        else:
            self.interest_rate = amount / 100
            self.balance += self.balance * self.interest_rate
            print(f'interest rate: {amount}%. New balance: {self.balance}')


# Создаем счета
checking = CheckingAccount("CA54321", "Bob", 500, 200)
saving = SavingsAccount('NU59669', 'Nurislam', 50, 500)

# Создаем банк и добавляем счета
bank = Bank("MyBank")
bank.add_account(checking)
bank.add_account(saving)

# Действия с счетами
checking.withdraw(600)
checking.deposit(300)
saving.add_interest(0)
saving.deposit(500)

# Выводим список счетов и общую сумму денег в банке
bank.list_accounts()
bank.total_funds()
