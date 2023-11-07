import random

class BankAccount:
    def __init__(self, full_name):
        # Initialize account properties
        self.full_name = full_name
        self.account_number = self.generate_account_number()  # Generate an 8 digit number account number
        self.balance = 0.0  # Initial balance = zero

    # Generate a random 8-digit account number
    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    # Deposit a given amount, update the balance, and display new balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            message = f"Amount deposited: ${amount:.2f}.\nNew Balance: ${self.balance:.2f}"
            return message
        else:
            return "Invalid deposit amount. Amount must be greater than 0"
        
    # Withdraw the given amount, update the balance, and display new balance or an overdraft fee
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Amount withdrawn: ${amount:.2f}.\nNew balance: ${self.balance:.2f}"
            else:
                self.balance -= 10.0
                return "Insufficient funds: $10 overdraft fee charged."
        else:
            return "Invalid withdrawal amount."

    # Print message and return current balance
    def get_balance(self):
        message = f"Account balance: ${self.balance:.2f}"
        print(message)
        return self.balance
    
    # Add monthly interest to balance, display updated balance, or notify if no interest is due
    def add_interest(self):
        if self.balance >= 1:
            monthly_interest = self.balance * 0.00083  # Calculate monthly interest based on the provided formula
            self.balance += monthly_interest
            return f"Monthly interest: ${monthly_interest:.2f}.\nNew balance: ${self.balance:.2f}"
        else:
            return "No monthly interest due to low account balance."

    # Print statement with the account holder's name, partially hidden account number, and current balance
    def print_statement(self):
        statement = f"{self.full_name}\nAccount Type: {self.account_type}\nAccount No.: ****{self.account_number[-4:]}\nBalance: ${self.balance:.2f}"
        return statement