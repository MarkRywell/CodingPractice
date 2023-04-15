# Problem 6
# Find the sum of all the multiples of 3 or 5 below 1000

number = 0
list1 = []
sum1 = 0


while number < 10:
    number += 1
    if number % 3 == 0 or number % 5 == 0:
        list1.append(number)
        sum1 = sum(list1)

print(sum1)
