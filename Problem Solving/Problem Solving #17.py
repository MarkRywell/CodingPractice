
arrNumbers = [5, 7, 2, 83, 12, 15]

num = int(input("Check the number: "))

a = 0

for a in arrNumbers:
    if a == num:
        print(arrNumbers.index(a))

