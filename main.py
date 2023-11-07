# Import the Bank class
from Bank import Bank

def main():
    # Instance of the Bank class
    bank = Bank()

    # Banking menu option
    while True:
        print("\n*******BankQuest********\nThe Financial Adventure!\n")
        print("[1] Account Creation")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Transfer")
        print("[5] Statement")
        print("[6] Exit")

        # Prompt user to enter selection
        choice = input("\nEnter your selection: ")

        # User's options based on previous selection
        # Account creation method and print result
        if choice == "1":
            full_name = input("Please enter your full name associated with the account: ")
            account_type = input("Please enter the account type (Checking or Savings): ")
            result = bank.create_account(full_name, account_type)
            print(result)
        
        # Deposit method and print result
        elif choice == "2":
            account_number = input("Please enter your 8-digit account number: ")
            amount = float(input("Please enter the deposit amount: "))
            print(bank.deposit(account_number, amount))

        # Withdraw method and print result
        elif choice == "3":
            account_number = input("Please enter your 8-digit account number: ")
            amount = float(input("Please enter the amount to withdraw: "))
            print(bank.withdraw(account_number, amount))

        # Transfer method and print result
        elif choice == "4":
            from_account_number = input("Please enter the source account number: ")
            to_account_number = input("Please enter the destination account number: ")
            amount = float(input("Please enter the amount to transfer: "))
            print(bank.transfer(from_account_number, to_account_number, amount))

        # Statement method and print result
        elif choice == "5":
            account_number = input("Please enter your 8-digit account number: ")
            print(bank.statement(account_number))

        # Exit application
        elif choice == "6":
            print("Exiting application.\nThank you for your business with BankQuest: The Financial Adventure!")
            break
        
        # Invalid option message
        else:
            print("Invalid option. Please make a valid selection.")


# Run main function
if __name__ == "__main__":
    main()