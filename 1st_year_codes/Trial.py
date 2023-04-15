a = [[1, 2, 3], [4, 5, 6]]
print(a[0])
print(a[1])
b = a[0]
print(a[0][2])
a[0][1] = 7
print(a)
print(b)
b[2] = 9
print(a[0])
print(b)

print("")

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end= '')
    print()

print("")

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

for row in a:
    for elem in row:
        print(elem,end='')
    print()

print("")

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
    print(s)