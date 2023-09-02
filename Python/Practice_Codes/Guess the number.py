from random import *

trials = 0

print("Guess the number!")
print()
print()

print("Easy:    1 - 10")
print("Medium:  1 - 20")
print("Hard:    1 - 40")


def try_again():
    pass


def easy():
    global trials
    trials = 3
    print()
    print("Easy Mode")
    print("Guess the number from 1 to 10")
    guess_num = randint(1, 11)

    answer = int(input("Guess the number:"))
    while answer < guess_num:
        print()
        trials -= 1
        print("Higher")
        print("Trials left: ", trials)
        print()
        answer = int(input("Guess the number:"))
    while answer > guess_num:
        print()
        print("Lower")
        answer = int(input("Guess the number:"))
    else:
        print()
        print("You guessed the number!: ", guess_num)
        try_again()


def medium():
    pass

def hard():
    pass


options = input("Choose difficulty level: ")
while options != "Easy" and options != "Medium" and options != "Hard":
    print("Invalid option")
    options = input("Choose difficulty level: ")

if options == "Easy":
    easy()
elif options == "Medium":
    medium()
elif options == "Hard":
    hard()









