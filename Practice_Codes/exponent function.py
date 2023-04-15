def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result



base = int(input("Enter base number: "))
power = int(input("Enter power number: "))

print(raise_to_power(base, power))

