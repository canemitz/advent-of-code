def part1(input_data):
    print('Q: In the output values, how many times do digits 1, 4, 7, or 8 appear?')
    input_data_list = parse_input_data(input_data)

    # Digits that use a certain number of segments (and no other digits do)
    # Key is number of segments, value is unique digit that uses that many segments
    signal_pattern_length_unique_digits = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }

    digit_appearances = {
        1: 0,
        4: 0,
        7: 0,
        8: 0
    }

    print(f'input_data_list:\n{input_data_list}')

    for dataset in input_data_list:
        print(f'dataset:\n{dataset}\n')
        signal_patterns = dataset[0].split(' ')
        output_value = dataset[1].split(' ')

        for output_value in output_value:
            try:
                digit = signal_pattern_length_unique_digits[len(output_value)]
                digit_appearances[digit] += 1
            except:
                pass

    ans = sum(digit_appearances.values())

    print(f'A: {ans}')


def parse_input_data(input_data):
    input_data_list = [x.split(' | ') for x in ''.join(input_data.readlines()).split('\n')]
    return input_data_list


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')
