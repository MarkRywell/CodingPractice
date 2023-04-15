def number_split(num):
    if(num % 2 == 0):
        result = num / 2
        return [int(result), int(result)]
    else:
        result = num / 2
        return [int(result), num-int(result)]


print(number_split(5))
print(number_split(10))