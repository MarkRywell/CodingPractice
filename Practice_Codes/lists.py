
colors = [["red", "yellow", "blue"], ["green", "orange", "violet"], ["black", "brown", "grey", "white"]]
print("Default list")

for i in range(len(colors)):
    for j in range(len(colors[i])):
        print(colors[i][j], end=" ")
    print()

print()
print("Edited List")
colors[1][2] = "purple"
colors[2].pop(3)
colors.insert(3, "lime")

for i in range(len(colors)):
    for j in range(len(colors[i])):
        print(colors[i][j], end=" ")
    print()

print()

print("Sorted List")
colors[0].sort()

for i in range(len(colors)):
    for j in range(len(colors[i])):
        print(colors[i][j], end=" ")
    print()

