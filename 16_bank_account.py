class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def show_details(self):
        return f'Account Owner: {self.owner}, Current Balance: {self.balance}'


jabir_bank = BankAccount('Jabir', 1000)

print(jabir_bank.show_details())