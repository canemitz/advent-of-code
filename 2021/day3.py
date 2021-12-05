def part1(diagnostic_report):
    print('Q: What is the power consumption of the submarine?')

    num_bits = 0
    bit_sums = []
    for binary_number in diagnostic_report:
        binary_number = binary_number.strip()

        # Create list of zeroes for each bit in binary number
        if not num_bits:
            num_bits = len(binary_number)
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

    ans = gamma * epsilon
    print(f'A: {ans}')


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')