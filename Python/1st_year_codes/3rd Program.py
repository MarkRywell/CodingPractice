lis = [2, 1, 3, 5, 4, 3, 8]

del lis[2:5]

print("List elements after deleting are :", end="")
for i in range(0, len(lis)):
    print(lis[i], end="")

print("\r")

lis.pop(2)

print("List elements after popping are: ", end="")
for i in range(0, len(lis)):
    print(lis[i], end="")
