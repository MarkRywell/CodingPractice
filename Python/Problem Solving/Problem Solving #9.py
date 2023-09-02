# Problem 9
# Accepts integers odd or even and returns the only odd or even integer in an array.

def odd_even(integers):
    odd = []
    even = []
    for numbers in integers:
        if numbers % 2 == 1:
            odd.append(numbers)
        elif numbers % 2 == 0:
            even.append(numbers)

    if len(odd) > len(even):
        return even[0]

    elif len(odd) < len(even):
        return odd[0]


print(odd_even([20, 40, 50, 62, 23, 52]))