class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        BankAccount.total_accounts += 1
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Balance cannot be negative!') 
        self._balance = value
    
    def show_details(self):
        return f'Account Owner: {self.owner}, Current Balance: {self.balance}'

    def deposit(self, n):
        if n <= 0:
            raise ValueError('Invalid deposit amount!')
        self.balance += n
        print(f'Deposit {n} successfully')

    def withdraw(self, n):
        if n > self.balance or n <= 0:
            raise ValueError('Insufficient balance or invalid amount!')
        self.balance -= n
        print(f'Withdraw {n} successfully')

    @classmethod
    def get_total_accounts(cls):
        return f'Total Bank Accounts: {cls.total_accounts}'



class SavingsAccount(BankAccount):
    def __init__(self,owner, balance):
        super().__init__(owner, balance)
    
    def add_interest(self, rate):
        self.balance += (self.balance * rate) / 100

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def withdraw(self, n):
        super().withdraw(n + 50)


account1 = BankAccount('Jabir', 1200)
account2 = BankAccount('Ahmad', 2400)

print(BankAccount.get_total_accounts())
# jabir_bank = BankAccount('Jabir', 1000)

# jabir_bank.deposit(500)
# jabir_bank.withdraw(100)
# print(jabir_bank.show_details())