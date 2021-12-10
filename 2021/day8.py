def part1(input_data):
    print('Q: In the output values, how many times do digits 1, 4, 7, or 8 appear?')
    input_data_list = parse_input_data(input_data)

    digit_appearances = {
        1: 0,
        4: 0,
        7: 0,
        8: 0
    }

    for dataset in input_data_list:
        signal_patterns = dataset[0].split(' ')
        output_value = dataset[1].split(' ')

        for output_value in output_value:
            unique_digit = get_digit_for_unique_pattern(output_value)
            if unique_digit is not None:
                digit_appearances[unique_digit] += 1

    ans = sum(digit_appearances.values())
    print(f'A: {ans}')


def parse_input_data(input_data):
    input_data_list = [x.split(' | ') for x in ''.join(input_data.readlines()).split('\n')]
    return input_data_list


def get_digit_for_unique_pattern(value):
    """Return digit if value has unique segment length"""

    # Mapping of number of segments to digits that are represented with that many segments
    signal_pattern_length_digits = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8]
    }

    digits = signal_pattern_length_digits[len(value)]
    if len(digits) == 1:
        unique_digit = digits[0]
    else:
        unique_digit = None

    return unique_digit


def part2(input_data):
    print('Q: What do you get if you add up all of the output values?')
    input_data_list = parse_input_data(input_data)

    output_values = []
    # Loop over the input data
    for dataset in input_data_list:
        signal_patterns = dataset[0].split(' ')
        output_value = dataset[1].split(' ')

        dataset_mapping = {}

        # Loop over the signal patterns and output value to determine the uniquely defined digits
        for val in signal_patterns+output_value:
            digit_for_pattern = get_digit_for_unique_pattern(val)

            # If pattern matches unique digit, set signal wire labels as value of digit key in dataset_mapping
            if digit_for_pattern:
                dataset_mapping[digit] = [signal_wire_label for signal_wire_label in val]

        signal_wire_labels = get_signal_wire_labels(dataset_mapping)

        # use that info to determine the non-unique [-ly defined by number of segments] digits
        remaining_signal_wire_labels = get_remaining_signal_wire_labels(signal_wire_labels, dataset)

        # ...which means we have all the labels now
        complete_signal_wire_labels = signal_wire_labels + remaining_signal_wire_labels

        # so, append the output value (using the derived labels) to our list of output_values
        output_values.append(get_output_value(complete_signal_wire_labels))

    ans = sum(output_values)
    print(f'A: {ans}')


def get_signal_wire_labels(dataset_mapping):
    # Having gotten all possible uniquely defined digits, determine which segments have which label
    # somethign something venn diagram
    # digit 1 has two wires
    # digit 7 has three wires
    # digit 4 has four wires
    # digit 8 has seven wires
    # given that info, and given dataset_mapping, loop over something (maybe multiple times)
    #  and figure out which signal wire (given correct positions a through g) has which incorrect/temporary label
    return signal_wire_labels


def get_remaining_signal_wire_labels(signal_wire_labels, dataset):
    # given signal wire labels gotten from uniquely defined digits...
    # ...get the other signal wire labels
    return remaining_signal_wire_labels


# def get_signal_pattern_digit_mapping(signal_patterns):
#     dataset_digit_mapping = {}

#     while len(dataset_digit_mapping) < 7:
#         for signal_pattern in signal_patterns:
#             digit = get_digit_for_unique_pattern(output_value)

#     return dataset_digit_mapping


# def get_base_7_segment_dict():
#     """Dictionary to hold the value for "correct" seven segment values."""
#     signal_pattern_length_unique_digits = {
#         2: 1,
#         3: 7,
#         4: 4,
#         7: 8
#     }
#     base_dict = {
#         'a': None,
#         'b': None,
#         'c': None,
#         'd': None,
#         'e': None,
#         'f': None,
#         'g': None,
#     }
#     return base_dict