def generate_combinations(prefix, length):
    # Define the characters to use for letters and numbers
    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'

    # Generate combinations
    combinations = []
    for letter1 in letters:
        for letter2 in letters:
            for number1 in numbers:
                for number2 in numbers:
                    for number3 in numbers:
                        for number4 in numbers:
                            combinations.append(f'{prefix}{letter1}{letter2}{number1}{number2}{number3}{number4}')

    return combinations

def write_to_file(filename, combinations):
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')

if __name__ == "__main__":
    # Set the starting prefix and length
    prefix = "PLDTWIFI"
    length = 4  # Change this value to adjust the length of the combinations

    # Generate combinations
    combinations = generate_combinations(prefix, length)

    # Write to file
    filename = "combinations1.txt"
    write_to_file(filename, combinations)

    print(f"Combinations written to {filename}")