# OOP-project

# Bank Account Simulator

A Python-based object-oriented banking simulator designed to demonstrate core programming concepts including class inheritance, exception handling, custom logic flow, and clean user interaction through method calls and print statements. This project simulates real-world banking operations such as deposits, withdrawals, transfers, and interest reward calculations across multiple account types.

# Features

-Base `BankAccount` class
  - Create accounts with starting balances
  - Deposit, withdraw, and transfer money
  - Balance validation using a custom `BalanceException` class

-Subclass `interestRewardsAcct`
  - Deposits earn a 5% bonus interest automatically
  - Inherits all features of the base class

-Subclass `savingsAcct`
  - Withdrawals include a fixed transaction fee ($5)
  - Overrides base methods with fee logic

-error handling
  - Prevents overdrafts using exception-based flow control
  - Gracefully interrupts transactions and provides clear feedback


# Skills Demonstrated

| Skill Area             | Description                                                                           |
|------------------------|-------------------------------------------------------------------------------------- |
| Object-Oriented Design | Defined clear class hierarchies (`BankAccount`, `interestRewardsAcct`, `savingsAcct`) |
| Exception Handling     | Implemented and invoked custom exception class (`BalanceException`)                   |
| Method Overriding      | Refined inherited behavior for deposit/withdraw across subclasses                     |
| Data Simulation        | Created multiple instances and executed financial operations                          |


# Future Enhancements

- Add logging support or GUI for visualization
- Include account history tracking
- Integration with file/database storage for persistent balance tracking
