import random

print("WELCOME TO RANDOM NUMBER GUESS GAME")


class Guess:
    def __init__(self, inp, ran):
        # Initialize the class with the user's input and the random number
        self.inp = inp
        self.ran = ran

    def play(self):
        # Start the game with the initial guess
        num = self.inp
        time = 1  # Initialize the number of attempts
        while num != self.ran and time > 0 and time < 5:
            # Continue the loop until the user guesses the correct number or runs out of attempts
            if num > self.ran:
                if num > 0:
                    print(f"You have {5 - time} more chances left.\n")
                num = int(
                    input("Guess a lower number: ")
                )  # Prompt the user to guess a lower number
            else:
                if num > 0:
                    print(f"You have {5 - time} more chances left.\n")
                num = int(
                    input("Guess a higher number: ")
                )  # Prompt the user to guess a higher number
            time += 1  # Increment the attempt counter

        # Check if the user guessed the correct number or ran out of attempts
        if num == self.ran:
            print("Congratulations! You win this game.")
        else:
            print("You lose")


# Generate a random integer between 1 and 9
random_number = random.randint(1, 9)
print("A random number between 1 and 9 has been generated.")

# Start the game with an initial guess from the user
initial_guess = int(input("Enter your guess: "))
game = Guess(initial_guess, random_number)
game.play()

# Sample Output:
# WELCOME TO RANDOM NUMBER GUESS GAME
# A random number between 1 and 9 has been generated.
# Enter your guess: 5
# You have 4 more chances left.
# Guess higher number: 7
# Congratulations! You win this game.
