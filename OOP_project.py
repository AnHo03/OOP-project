from bank_accounts import *

Andrew = BankAccount(1000,'Andrew')
Jenah = BankAccount(2000,'Jenah')

Andrew.getBalance()
Jenah.getBalance()

Jenah.deposit(500)

Andrew.withdraw(10000)
Andrew.withdraw(50)

Andrew.transfer(10000, Jenah)
Andrew.transfer(100,Jenah)

Tulip = intrestRewardsAcct(1000,'Tulip')
Tulip.getBalance()
Tulip.deposit(100)
Tulip.transfer(100, Jenah)

Daisy = savingsAcct(1000, 'Daisy')
Daisy.getBalance
Daisy.deposit(100)
Daisy.transfer(1000,Jenah)