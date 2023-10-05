# Define a class called "Account" to represent a bank account.
class Account:
    def __init__(self, username, password):
        self.username = username.lower()
        self.password = password

    # A method to check if the provided password matches the account's password.
    def check_password(self, password):
        return self.password == password

# Define a class called "Operation" to represent bank operations like withdrawals and deposits.


class Operation:
    def __init__(self, available_balance, withdraw_amount, deposit_amount):
        self.available_balance = available_balance
        self.withdraw_amount = withdraw_amount
        self.deposit_amount = deposit_amount

    # A method to display information about an operation.
    def display_info(self):
        print("---------------")
        print(f"Available Balance: {self.available_balance}")
        print(f"Withdraw Amount: {self.withdraw_amount}")
        print(f"Deposit Amount: {self.deposit_amount}")


# Create an empty list to store account objects.
accounts = []

# Initialize the current_account variable to None.
current_account = None

# Create an infinite loop for the banking application.
while True:
    print("-------------------------------")
    print("\nWelcome to JAIBANK. Please select an option:\n")
    print("-------------------------------")
    print("1. Create account\n2. Login\n3. Help")
    option = input("Enter your choice: ")

    # Check if the option input is not empty.
    if not option:
        raise ValueError("Option cannot be empty")

    option = int(option)

    if option == 1:
        # Gather information to create a new account.
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        contact_number = input("Enter your contact number: ")
        username = input("Create a username: ")
        password = input("Create a password: ")

        # Check if all required fields are filled.
        if not (first_name and last_name and contact_number and username and password):
            raise ValueError("All fields must be filled")

        # Check if the contact number is valid (10 digits and all digits).
        if len(contact_number) != 10 or not contact_number.isdigit():
            raise ValueError("Invalid Phone Number")

        # Create a new account object and add it to the accounts list.
        accounts.append(Account(username, password))
        print("Account created successfully. Please log in with your credentials.")
    elif option == 2:
        # Log in to an existing account.
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username and password are not empty.
        if not (username and password):
            raise ValueError("Username and password cannot be empty")

        # Iterate through the accounts to find a matching account.
        for account in accounts:
            if account.username == username and account.check_password(password):
                current_account = account
                print(f"{username} has logged in successfully")
                break
        if current_account is None:
            print("Invalid username or password")
        else:
            print("Bank Services:")
            break
    elif option == 3:
        # Display help information and exit the program.
        print("Please contact the helpline number \"1800112233\"")
        break
    else:
        print("Invalid option")

# Initialize the balance and operations variables for the logged-in account.
balance = 90000
operations = []

# Create an infinite loop for banking operations.
while True:
    if current_account is not None:
        print("\nWelcome to JAIBANK")
        print("1. Balance enquiry")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Mini Statement")
        print("5. Exit")
        option = input("Enter your choice: ")

        # Check if the option input is not empty.
        if not option:
            raise ValueError("Option cannot be empty")

        option = int(option)

        if option == 1:
            # Display the account balance.
            print("Your balance is:", balance, "rs/-")
        elif option == 2:
            # Withdraw funds from the account.
            withdraw_amount = input("Enter the withdrawal amount: ")

            if not withdraw_amount:
                raise ValueError("Withdrawal amount cannot be empty")

            withdraw_amount = int(withdraw_amount)

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print("Your updated balance is:", balance)
                operations.append(Operation(balance, withdraw_amount, 0))
            else:
                print("Insufficient balance")
        elif option == 3:
            # Deposit funds into the account.
            deposit_amount = input("Enter the deposit amount: ")

            if not deposit_amount:
                raise ValueError("Deposit amount cannot be empty")

            deposit_amount = int(deposit_amount)
            print("Your previous balance is:", balance)
            balance += deposit_amount
            print("Your updated balance is:", balance)
            operations.append(Operation(balance, 0, deposit_amount))
        elif option == 4:
            # Display a mini statement of recent operations.
            print("Mini Statement:")
            for operation in operations:
                operation.display_info()
                print("-------Thank You-------")
        elif option == 5:
            # Exit the banking application.
            print("Exiting...\n")
            print("Thank you for choosing JAIBANK as your banking partner")
            break
        else:
            print("Please select a valid option")


# #Output:
# Welcome to JAIBANK. Please select an option:
#
# -------------------------------
# 1. Create account
# 2. Login
# 3. Help
# Enter your choice: 1
# Enter your first name: Jai
# Enter your last name: Deep
# Enter your contact number: 0987654321
# Create a username: Jai
# Create a password: 123
# Account created successfully. Please log in with your credentials.
# -------------------------------
#
# Welcome to JAIBANK. Please select an option:
#
# -------------------------------
# 1. Create account
# 2. Login
# 3. Help
# Enter your choice: 2
# Enter your username: jai
# Enter your password: 123
# jai has logged in successfully
# Bank Services:
#
# Welcome to JAIBANK
# 1. Balance enquiry
# 2. Withdraw
# 3. Deposit
# 4. Mini Statement
# 5. Exit
# Enter your choice: 3
# Enter the deposit amount: 10000
# Your previous balance is: 90000
# Your updated balance is: 100000
#
# Welcome to JAIBANK
# 1. Balance enquiry
# 2. Withdraw
# 3. Deposit
# 4. Mini Statement
# 5. Exit
# Enter your choice: 2
# Enter the withdrawal amount: 20000
# Your updated balance is: 80000
#
# Welcome to JAIBANK
# 1. Balance enquiry
# 2. Withdraw
# 3. Deposit
# 4. Mini Statement
# 5. Exit
# Enter your choice: 4
# Mini Statement:
# ---------------
# Available Balance: 100000
# Withdraw Amount: 0
# Deposit Amount: 10000
# -------Thank You-------
# ---------------
# Available Balance: 80000
# Withdraw Amount: 20000
# Deposit Amount: 0
# -------Thank You-------
#
# Welcome to JAIBANK
# 1. Balance enquiry
# 2. Withdraw
# 3. Deposit
# 4. Mini Statement
# 5. Exit
# Enter your choice: 5
# Exiting...
#
# Thank you for choosing JAIBANK as your banking partner
