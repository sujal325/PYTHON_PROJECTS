import random

print("WELCOME TO SNAKE WATER GUN GAME\n")


def game():

    while 1 > 0:
        user = input("choose (SNAKE, GUN OR WATER):")
        choice = ["snake", "water", "gun"]

        random_choice = random.choice(choice)
        if random_choice == user:

            print(f"Game tie you choose {user} and computer choose {random_choice}\n")
        elif (
            (random_choice == "snake" and user == "water")
            or (random_choice == "water" and user == "gun")
            or (random_choice == "gun" and user == "snake")
        ):

            print(f"Game loose you choose {user} and computer choose {random_choice}\n")
        elif (
            (random_choice == "water" and user == "snake")
            or (random_choice == "gun" and user == "water")
            or (random_choice == "snake" and user == "gun")
        ):

            print(f"Game win you choose {user} and computer choose {random_choice}\n")


game()
