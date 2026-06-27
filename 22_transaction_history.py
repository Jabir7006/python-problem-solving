class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        BankAccount.total_accounts += 1
        self.history = []
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
        self.history.append(f'Deposited: {n}')
        print(f'Deposit {n} successfully')

    def withdraw(self, n):
        if n > self.balance or n <= 0:
            raise ValueError('Insufficient balance or invalid amount!')
        self.balance -= n
        self.history.append(f'Withdrew: {n}')
        print(f'Withdraw {n} successfully')

    @classmethod
    def get_total_accounts(cls):
        return f'Total Bank Accounts: {cls.total_accounts}'

    def show_history(self):
        if self.history:
            for h in self.history:
                print(h)
        else:
            print('No transactions yet.')



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



class Customer:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email 
        self.account = account
    
    def get_customer_info(self):
        return f'Customer Name: {self.name} \nCustomer Email: {self.email} \nAccount Balance: {self.account.balance}'
    
    

account1 = BankAccount('Jabir', 1200)
account1.deposit(500)
account1.withdraw(100)
account1.show_history()

