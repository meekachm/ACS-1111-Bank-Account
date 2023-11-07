# Import the BankAccount class
from BankAccount import BankAccount

class Bank:
    def __init__(self):
        # Initialize empty list to store accounts
        self.accounts = []

    # Account creation method
    def create_account(self, full_name, account_type):
        new_account = BankAccount(full_name, account_type)
        # Append new account to list of accounts
        self.accounts.append(new_account)
        return f"Account created successfully.\nYour new account number is: {new_account.account_number}"

    # Deposit method and return result
    def deposit(self, account_number, amount):
        # Iterate through the accounts to find the matching account number
        for account in self.accounts:
            if account.account_number == account_number:
                return account.deposit(amount)
        # If failed to find account, return message
        return "Account Not Found."

    # Wthdraw method on account and return result
    def withdraw(self, account_number, amount):
        # Iterate through the accounts to find the matching account number
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        # If failed to find account, return message
        return "Account Not Found."

    # Transfer method and return result
    def transfer(self, from_account_number, to_account_number, amount):
        # Iterate through the accounts to find the source account with the matching account number
        for from_account in self.accounts:
            if from_account.account_number == from_account_number:
                # Iterate through the accounts to find the destination account with the matching account number
                for to_account in self.accounts:
                    if to_account.account_number == to_account_number:
                        # Attempt to withdraw from the source account
                        if from_account.withdraw(amount) == "Insufficient funds: $10 overdraft fee charged.":
                            return "Transfer Failed: Insufficient funds in the source account."
                        else:
                            # If withdrawal is successful, deposit amount into destination account
                            to_account.deposit(amount)
                            return "Transfer Successful."
        # If failed to find account, return message
        return "Account(s) Not Found."

    # Print statement method and return the result
    def statement(self, account_number):
        # Iterate through the accounts to find the matching account number
        for account in self.accounts:
            if account.account_number == account_number:
                return account.print_statement()
        # If failed to find account, return message
        return "Account Not Found."