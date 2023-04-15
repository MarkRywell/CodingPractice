
secret_word = "mark"

guess_word = ""

count = 3
print("You can only have 3 trials")
print()
while guess_word != secret_word:
    guess_word = input("Guess the word: ")
    print()
    if guess_word == secret_word:
        break
    count -= 1
    print(str(count) + " trial/s left")
    print()
    if count == 0:
        print("You lose the game!")
        exit()
print("You win the game!!")
