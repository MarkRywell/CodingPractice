number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for y in range(len(number_grid)):
    for x in range(len(number_grid[y])):
        print(number_grid[y][x], end=" ")
    print()

print("=======================")

for row in number_grid:
    for column in row:
        print(column)
