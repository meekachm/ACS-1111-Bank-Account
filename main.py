# Import the BankAccount class
from BankAccount import BankAccount

def main():
    bank = {}

    while True:
        print("\n*******BankQuest********\nThe Financial Adventure!\n")
        print("[1] Account Creation")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Statement")
        print("[5] Exit")

        # Prompt user to enter selection
        choice = input("\nEnter your selection: ")

        # User's options based on previous selection
        if choice == "1":
            full_name = input("Please enter your full name associated with the account: ")
            account_number = input("Please enter your 8-digit account number: ")
            balance = float(input("Please enter the initial balance for your account: "))

            # Create a new BankAccount instance and store it in the bank dictionary
            bank[account_number] = BankAccount(full_name, account_number, balance)
            print("Account created successfully.")
            
            # Prompt user to enter selection
            choice = input("\nEnter your selection: ")

        elif choice == "2":
            account_number = input("Please enter your 8-digit account number: ")
            if account_number in bank:
                amount = float(input("Please enter the deposit amount: "))
                print(bank[account_number].deposit(amount))
            else:
                print("Account not found.")
            
            # Prompt user to enter selection
            choice = input("\nEnter your selection: ")

        elif choice == "3":
            account_number = input("Please enter your 8-digit account number: ")
            if account_number in bank:
                amount = float(input("Please enter the amount to withdraw: "))
                print(bank[account_number].withdraw(amount))
            else:
                print("Account not found.")

            # Prompt user to enter selection
            choice = input("\nEnter your selection: ")

        if choice == "4":
            account_number = input("Please enter your 8-digit account number: ")
            if account_number in bank:
                print(bank[account_number].print_statement())
            else:
                print("Account not found.")

            # Prompt user to enter selection
            choice = input("\nEnter your selection: ")

        elif choice == "5":
            print("Exiting application.\nThank you for your business with BankQuest: The Financial Adventure!")
            break

        else:
            print("Invalid option. Please make a valid selection.")

if __name__ == "__main__":
    main()
