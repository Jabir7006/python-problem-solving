class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
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

jabir_bank = BankAccount('Jabir', 1000)

jabir_bank.deposit(500)
jabir_bank.withdraw(100)
print(jabir_bank.show_details())