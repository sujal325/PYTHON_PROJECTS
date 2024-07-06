import random

print("WELCOME TO RANDOM NUMBER GUESS GAME")


class guess:
    def __init__(self, inp, ran):
        self.inp = inp
        self.ran = ran

    def play(self):
        num = self.inp
        time = 1
        while num != self.ran and time > 0 and time < 5:
            if num > self.ran:
                if num > 0:
                    print(f"You have {5 - time} more chance left.\n")
                num = int(input("Guess lower number: "))
            else:
                if num > 0:
                    print(f"You have {5 - time} more chance left.\n")
                num = int(input("Guess higher number: "))
            time += 1
        if num == self.ran:
            print("Congratulation you win this game.")
        else:
            print("You loose")


a = int(input("random number: "))
b = random.randint(1, 9)
s = guess(a, b)
s.play()
