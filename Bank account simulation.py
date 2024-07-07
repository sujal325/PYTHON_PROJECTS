# Print a welcome message for the bank account simulation.
print("Welcome to my bank account simulation.\n")

# Print the options available for the user.
print(
    """TYPE
       1 for deposit
       2 for withdraw
       3 for check balance
       0 for exit
    """
)


# Define a class named `bank` to represent the bank account.
class bank:
    def __init__(self, amount=1000):
        self.account = (
            amount  # Initialize the account balance with a default amount of 1000.
        )

    def deposit(self, amount):
        self.account += amount  # Add the deposited amount to the account balance.
        print(
            f"You deposit: {amount} amount.\n"
        )  # Print a message confirming the deposit.

    def withdraw(self, amount):
        self.account -= (
            amount  # Subtract the withdrawn amount from the account balance.
        )
        print(
            f"Your withdraw: {amount} amount.\n"
        )  # Print a message confirming the withdrawal.

    def check_balance(self):
        print(f"Your balance is {self.account}\n")  # Print the current account balance.


# Initialize variables for user input and create an instance of the bank class.
amo = 0
abc = bank()

# Start an infinite loop to interact with the user until the user chooses to exit (condition 0).
while True:
    condition = int(
        input("What do you want to do: ")
    )  # Prompt the user to choose an action.

    if condition == 1:
        amo = int(input("Type amount: "))  # Prompt for the amount to deposit.
        abc.deposit(amo)  # Call the deposit method of the `bank` class instance.
    elif condition == 2:
        amo = int(input("Type amount: "))  # Prompt for the amount to withdraw.
        abc.withdraw(amo)  # Call the withdraw method of the `bank` class instance.
    elif condition == 3:
        abc.check_balance()  # Call the check_balance method of the `bank` class instance.
    elif condition == 0:
        break  # Exit the loop and end the program if condition is 0.
    else:
        print(
            "Sorry! we don't have that feature now."
        )  # Print a message for invalid input.

# End of the program.
