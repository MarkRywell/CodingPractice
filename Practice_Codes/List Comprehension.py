# Multiply by 2 the every element of a
# Square the every element of a list

a = [1, 3, 5, 7, 9, 11]

b = [x * 2 for x in a]

for element in b:
    print(element, end=" ")

c = [x ** 2 for x in range(1, 7)]

print()
for element in c:
    print(element, end=" ")

d = [x ** 2 for x in reversed(range(1, 7))]

print()
for element in d:
    print(element, end=" ")

e = [x ** 2 for x in range(6, 0, -1)]

print()
for element in e:
    print(element, end=" ")