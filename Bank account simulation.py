print("Welcome to my bank account simulation.\n")
print(
    """TYPE
       1 for deposit
       2 for withdraw
       3 for check balance
       0 for exit
    """
)


class bank:
    def __init__(self, amount=1000):
        self.account = amount

    def deposit(self, amount):
        self.account += amount
        print(f"You deposit: {amount} amount.\n")

    def withdraw(self, amount):
        self.account -= amount
        print(f"Your withdraw: {amount} amount.\n")

    def check_balance(self):
        print(f"Your balance is {self.account}\n")


amo = 0
abc = bank()
while True:
    condition = int(input("What do you want to do: "))
    if condition == 1:
        amo = int(input("Type amount: "))
        abc.deposit(amo)
    elif condition == 2:
        amo = int(input("Type amount: "))
        abc.withdraw(amo)
    elif condition == 3:
        abc.check_balance()
    elif condition == 0:
        break
    else:
        print("Sorry! we don't have that feature now.")
