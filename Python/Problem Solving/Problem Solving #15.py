# Problem 15

y = [6, 4, 2]

y.extend([12, 8, 4])
y[1] = 3

print(y)

x = [1, 3, 5, 6, 7, 8, 4, 5, 6, 3, 3, 2, 3, 4, 5, 1, 2, 4, 6]

for number in x:
    if x[number] == x[number]:
        x.remove(number)

x.sort()
print(x)