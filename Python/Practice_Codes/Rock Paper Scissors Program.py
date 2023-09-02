import random


def rps():
    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print("The user chose", user)
    print("The computer chose", comp)
    print()

    print()
    if user == 'rock' and comp == 'rock':
        print("DRAW!")
    elif user == 'rock' and comp == 'scissors':
        print("YOU WIN!")
    elif user == 'rock' and comp == 'paper':
        print("YOU LOSE!")
        print("Better luck next time")
    elif user == 'paper' and comp == 'paper':
        print("DRAW!")
    elif user == 'paper' and comp == 'rock':
        print("YOU WIN!")
    elif user == 'paper' and comp == 'scissors':
        print("YOU LOSE!")
        print("Better luck next time")
    elif user == 'scissors' and comp == 'scissors':
        print("DRAW!")
    elif user == 'scissors' and comp == 'paper':
        print("YOU WIN!")
    elif user == 'scissors' and comp == 'rock':
        print("YOU LOSE!")
        print("Better luck next time")

    print()

    again = input("Play again? Yes/No:  ")
    if again == 'Yes':
        rps()
    else:
        return


rps()
