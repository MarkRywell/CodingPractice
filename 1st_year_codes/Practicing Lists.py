
tech = [['huawei', 'samsung', 'redmi'], ['dell', 'hp', 'asus'], ['msi', 'gigabyte', 'amd']]

for i in range(len(tech)):
    for j in range(len(tech[i])):
        print(tech[i][j], end="")
    print()