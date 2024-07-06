import random

print("WELCOME TO SNAKE WATER GUN GAME\n")


def game():
    while True:
        # Prompt the user to choose between Snake, Water, or Gun
        user = input("Choose (SNAKE, GUN, OR WATER): ").lower()
        choice = ["snake", "water", "gun"]

        # Randomly select the computer's choice
        random_choice = random.choice(choice)

        if random_choice == user:
            # If both choices are the same, it's a tie
            print(
                f"Game tie! You chose {user} and the computer chose {random_choice}\n"
            )
        elif (
            (random_choice == "snake" and user == "water")
            or (random_choice == "water" and user == "gun")
            or (random_choice == "gun" and user == "snake")
        ):
            # Conditions where the user loses
            print(
                f"Game lose! You chose {user} and the computer chose {random_choice}\n"
            )
        elif (
            (random_choice == "water" and user == "snake")
            or (random_choice == "gun" and user == "water")
            or (random_choice == "snake" and user == "gun")
        ):
            # Conditions where the user wins
            print(
                f"Game win! You chose {user} and the computer chose {random_choice}\n"
            )


game()

# Sample Output:
# WELCOME TO SNAKE WATER GUN GAME

# Choose (SNAKE, GUN, OR WATER): snake
# Game win! You chose snake and the computer chose water
