# Import the BankAccount class
from BankAccount import BankAccount

# Stretch Challenges 2: Create a list called: bank. 
bank = []

# 5. Define 3 different bank account examples using various methods
# Example 1: Create a new bank account for "Haruki Nakamura"
haruki_account = BankAccount("Haruki Nakamura")
haruki_account.deposit(1500)  # Deposit $1500
haruki_account.get_balance()  # Get the account balance
haruki_account.add_interest()  # Add interest
haruki_account.get_balance()  # Get the account balance
haruki_account.withdraw(300)  # Make a withdrawal
haruki_account.get_balance()  # Get the account balance

# Example 2: Create a new bank account for "Hyejin Lee"
hyejin_account = BankAccount("Hyejin Lee")
hyejin_account.deposit(2000)  # Deposit $2000
hyejin_account.get_balance()  # Get the account balance
hyejin_account.add_interest()  # Add interest
hyejin_account.get_balance()  # Get the account balance
hyejin_account.withdraw(400)  # Make a withdrawal
hyejin_account.get_balance()  # Get the account balance

# Example 3: Create a new bank account for "WeiLi Chen"
weili_account = BankAccount("WeiLi Chen")
weili_account.deposit(2500)  # Deposit $2500
weili_account.get_balance()  # Get the account balance
weili_account.add_interest()  # Add interest
weili_account.get_balance()  # Get the account balance
weili_account.withdraw(600)  # Make a withdrawal
weili_account.get_balance()  # Get the account balance


# Stretch Challenges 2: Add all accounts to the "bank" list
bank.append(haruki_account)
bank.append(hyejin_account)
bank.append(weili_account)


# 6. Creating a new bank account for "Mitchell" with an initial balance of $0
mitchell_account = BankAccount("Mitchell", account_number="03141592")
# Depositing $400,000 into "Mitchell's" account
mitchell_account.deposit_amount = 400000
# Printing a statement
mitchell_account.print_statement()
# Adding interest to the account
mitchell_account.add_interest()
# Printing a statement
mitchell_account.print_statement()
# Making a withdrawal of $150 from Mitchell's account
mitchell_account.withdraw(150)
# Printing a statement
mitchell_account.print_statement()


# Stretch Challenges 1: Print a statement for each account
# Example 1: Saving Account for "Wirakorn Suwan"
wirakorn_account = BankAccount("Wirakorn Suwan", "Savings")
wirakorn_account.deposit(1200)
wirakorn_account.add_interest()
# Use print() to display the statement
print(wirakorn_account.print_statement())

# Example 2: Checking Account for "Kenji Suzuki"
kenji_account = BankAccount("Kenji Suzuki", "Checking")
kenji_account.deposit(650)
kenji_account.add_interest()
# Use print() to display the statement
print(kenji_account.print_statement())


# Stretch Challenges 2: Function that loops over all accounts in the "bank" list 
# and calls the add interest
def add_interest_to_accounts(bank):
    for account in bank:
        account.add_interest()

# Call the function to add interest to all accounts in the "bank" list
add_interest_to_accounts(bank)