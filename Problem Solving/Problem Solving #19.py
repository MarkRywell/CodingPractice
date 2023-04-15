def missing_letters(letters):
    temp = 0
    for letter in reversed(letters):
        if letter == letters[len(letters) - 1]:
            temp = ord(letter)
            continue
        temp = temp - ord(letter)

        if temp > 1:
            if letter.isupper():
                return chr((ord(letter) + 1)).upper()
            return chr((ord(letter) + 1))
        temp = ord(letter)


print(missing_letters(['A', 'B', 'D']))
