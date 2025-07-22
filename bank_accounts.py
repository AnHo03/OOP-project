class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, intitialAmmount, acctName):
        self.balance = intitialAmmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' ballance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("deposit complete")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"sorry {self.name} only has a balance of ${self.balance}")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nwithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interuppted {error}")

    def transfer(self,amount, account):
        try:
            print("\nBeginning Transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete')

        except BalanceException as error:
            print(f'\nTransfer interupted. {error}')

class intrestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("Deposit complete.")
        self.getBalance()

class savingsAcct(intrestRewardsAcct):
    def __init__(self, initialAmount, acctname):
        super().__init__(initialAmount, acctname)
        self.fee = 5

    def withdraw (self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nwithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw intterupted: {error}")
        
