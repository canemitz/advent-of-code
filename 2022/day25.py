def part1(puzzle_input):
    print("Q: The Elves are starting to get cold. What SNAFU number do you supply to Bob's console?")

    total_fuel_needed = 0
    for fuel_requirement in puzzle_input:
        total_fuel_needed += snafu_to_decimal(fuel_requirement)

    ans = decimal_to_snafu(total_fuel_needed)

    print(f'A: {ans}')


def snafu_to_decimal(snafu_number):
    decimal_number = 0

    for power_of_five in range(len(snafu_number)):
        place_value = 5**power_of_five
        snafu_sub_value = snafu_number[ -(power_of_five+1) ]
        if snafu_sub_value == '=':
            snafu_sub_value = -2
        elif snafu_sub_value == '-':
            snafu_sub_value = -1
        else:
            snafu_sub_value = int(snafu_sub_value)

        decimal_number += place_value*snafu_sub_value

    return decimal_number


def decimal_to_snafu(decimal_number):
    # Convert decimal number to list of base 5 place values
    base_5 = []

    # TODO: handle negative numbers
    while decimal_number:
        base_5.insert(0, int(decimal_number % 5))
        decimal_number //= 5

    # Replace all digits greater than 2
    while [digit for digit in base_5 if digit > 2]:
        for i in range(len(base_5)-1, -1, -1):
            # Add one to digit to the left, inserting into a new place value if needed
            digit = base_5[i]
            if digit > 2:
                try:
                    base_5[i-1] += 1
                except:
                    base_5.insert(0, 1)

            # Subtract the correct amount from the current digit
            if digit == 3:
                base_5[i] = -2
            elif digit == 4:
                base_5[i] = -1
            elif digit == 5:
                base_5[i] = 0

    # Convert negative numbers to their symbolic minus and double-minus representations
    for i in range(len(base_5)):
        digit = base_5[i]
        if digit == -1:
            base_5[i] = '-'
        elif digit == -2:
            base_5[i] = '='

    snafu_number = ''.join([ str(digit) for digit in base_5 ])
    return snafu_number