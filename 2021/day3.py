def part1(diagnostic_report):
    print('Q: What is the power consumption of the submarine?')

    num_bits = len(diagnostic_report.readline().strip())
    bit_sums = []
    for binary_number in diagnostic_report:
        binary_number = binary_number.strip()

        # Create list of zeroes for each bit in binary number
        if not bit_sums:
            bit_sums = [0 for x in range(num_bits)]

        # Add/subtract 1 to each element in bit_sums if bit is 1/0
        for i, bit in enumerate(binary_number):
            if bit == '1':
                bit_sums[i] += 1
            else:
                bit_sums[i] -= 1

    gamma_binary   = ''
    epsilon_binary = ''

    for bit_sum in bit_sums:
        if bit_sum > 0:
            gamma_binary   += '1'
            epsilon_binary += '0'
        else:
            gamma_binary   += '0'
            epsilon_binary += '1'

    gamma   = int(gamma_binary, 2)
    epsilon = int(epsilon_binary, 2)

    power_consumption = gamma * epsilon
    print(f'A: {power_consumption}')


def part2(diagnostic_report):
    print('Q: What is the life support rating of the submarine?')

    diagnostic_report = [x.strip() for x in diagnostic_report.readlines()]

    num_bits = len(diagnostic_report[0])

    oxygen_generator_rating = None
    co2_scrubber_rating = None

    # Find oxygen generator rating
    remaining_numbers = diagnostic_report
    for bit_position in range(num_bits):
        most_common_bit = get_most_common_bit(remaining_numbers, bit_position)
        remaining_numbers = [x for x in remaining_numbers if x[bit_position] == str(most_common_bit)]

        if len(remaining_numbers) == 1:
            oxygen_generator_rating = int(remaining_numbers[0], 2)
            break

    # Find co2_scrubber rating
    remaining_numbers = diagnostic_report
    for bit_position in range(num_bits):
        least_common_bit = get_least_common_bit(remaining_numbers, bit_position)
        remaining_numbers = [x for x in remaining_numbers if x[bit_position] == str(least_common_bit)]

        if len(remaining_numbers) == 1:
            co2_scrubber_rating = int(remaining_numbers[0], 2)
            break

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(f'A: {life_support_rating}')


def get_most_common_bit(list_of_numbers, bit_position):
    bit_sum = 0

    for binary_number in list_of_numbers:
        if binary_number[bit_position] == '1':
            bit_sum += 1
        else:
            bit_sum -= 1

    if bit_sum < 0:
        most_common_bit = 0
    else:
        most_common_bit = 1

    return most_common_bit


def get_least_common_bit(list_of_numbers, bit_position):
    bit_sum = 0

    for binary_number in list_of_numbers:
        if binary_number[bit_position] == '1':
            bit_sum += 1
        else:
            bit_sum -= 1

    if bit_sum < 0:
        least_common_bit = 1
    else:
        least_common_bit = 0

    return least_common_bit