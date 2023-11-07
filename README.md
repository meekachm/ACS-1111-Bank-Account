# ACS-1111 Bank Account Assignment

# BankQuest: The Financial Adventure

The **BankQuest** project is an engaging exploration of object-oriented programming (OOP) concepts using Python, with a focus on banking functionalities. This README provides an overview of the project and its key components.

## Project Structure

The project consists of several Python files, each serving a specific purpose:

### main.py

This is the main application script, responsible for user interaction. It imports the `Bank` class and presents a menu-driven interface for users to perform various banking operations. The available options include account creation, deposits, withdrawals, transfers, statement viewing, and exiting the application.

### BankAccount.py

The `BankAccount` class is defined in this file. It represents a bank account with attributes for full name, account type, account number, and balance. The class also provides methods for depositing funds, making withdrawals (including overdraft handling), checking the balance, calculating and adding interest, and printing an account statement.

### Bank.py

The `Bank` class is found in this file. It manages a list of `BankAccount` instances and offers methods for creating accounts, depositing, withdrawing, transferring funds, and viewing statements.

### ExampleAccounts.py

This file contains example accounts and demonstrates various operations, such as creating accounts, making deposits, adding interest, and more. It also includes functions to add interest to accounts and print statements.