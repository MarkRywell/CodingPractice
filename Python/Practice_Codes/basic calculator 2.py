count = 0
i = 0
numbers = []
number = 0

try:
    count = int(input("Count: "))
except:
    print("Invalid Input")

while i != count:
    try:
        number = int(input("Enter a number: "))
        numbers.append(number)
        i += 1
    except:
        print("Invalid Input")

print()

for x in numbers:
    if x == numbers[-1]:
        print(x, end=" ")
    else:
        print(x, end=" + ")
print()

print()

print("Sum: ", sum(numbers))
