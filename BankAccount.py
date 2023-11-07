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
