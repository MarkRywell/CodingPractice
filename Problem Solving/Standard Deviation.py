import math

def calculate(data):
    mean = sum(data) / len(data)
    sumof = 0
    for num in data:
        sumof += ((num - mean) ** 2)
    SD = math.sqrt(sumof / len(data))

    return round(SD, 2)

print(calculate([0,1,0,6,5,6,5,9,8,6,9,44]))



