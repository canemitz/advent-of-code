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
        output_value_patterns = dataset[1].split(' ')

        # Determine the segment label sets for each improperly labeled digit
        digit_segment_sets = get_digit_segment_sets(signal_patterns)

        # Use the digit_segment_sets to find the output_value
        output_value_str = ''
        for pattern in output_value_patterns:
            pattern_set = set(pattern)

            # Append to output_value_str the digit whose segment set matches this pattern set
            for digit, digit_segment_set in digit_segment_sets.items():
                if digit_segment_set == pattern_set:
                    output_value_str += str(digit)
                    break

        output_values.append(int(output_value_str))

    ans = sum(output_values)
    print(f'A: {ans}')


def get_unique_digit_segment_sets(signal_patterns):
    """Return dictionary of digits (which have unique signal patterns)
       keyed to the sets of segment labels that correspond to them.
    """
    unique_digit_segment_sets = {}

    for signal_pattern in signal_patterns:
        unique_digit = get_digit_for_unique_pattern(signal_pattern)

        # If digit is uniquely defined, add set of signal wire labels to the dictionary
        if unique_digit:
            unique_digit_segment_sets[unique_digit] = {segment_label for segment_label in signal_pattern}

        # Stop if we already have the segment sets for each uniquely defined digit
        if len(unique_digit_segment_sets) == 4:
            break

    return unique_digit_segment_sets


def get_segment_mapping(signal_patterns):
    # Mapping of "proper" segment label to currently-active segment label
    segment_mapping = {}

    digit_segment_sets = get_unique_digit_segment_sets(signal_patterns)

    # The segment label appearing in 7, but not in 1, is the proper 'a' segment
    for segment_label in digit_segment_sets[7]:
        if segment_label not in digit_segment_sets[1]:
            segment_mapping['a'] = segment_label
            break
    # segment_mapping.keys() == ['a']

    # There are three digits with six segments: 0, 6, and 9
    # The segment labels not in all three sets are the proper 'c', 'd', and 'e' segments
    segment_sets_069 = []
    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 6:
            segment_sets_069.append({segment_label for segment_label in signal_pattern})
    segment_sets_069_union = set.union(segment_sets_069[0], segment_sets_069[1], segment_sets_069[2])
    segment_sets_069_intersection = set.intersection(segment_sets_069[0], segment_sets_069[1], segment_sets_069[2])
    segments_cde = segment_sets_069_union - segment_sets_069_intersection

    # The segment label in 7, and in segments_cde, is proper 'c'
    segment_mapping['c'] = digit_segment_sets[7].intersection(segments_cde).pop()
    # segment_mapping.keys() == ['a', 'c']

    # The segment label in 4, and in segments_cde, that does not map to proper 'c', is proper 'd'
    segment_mapping['d'] = digit_segment_sets[4].intersection(segments_cde).difference({segment_mapping['c']}).pop()
    # segment_mapping.keys() == ['a', 'c', 'd']

    # The segment label in segments_cde, that does not map to proper 'c' or 'd', is proper 'e'
    segment_mapping['e'] = segments_cde.difference({segment_mapping['c'], segment_mapping['d']}).pop()
    # segment_mapping.keys() == ['a', 'c', 'd', 'e']

    # The segment label in 1, that does not map to proper 'c', is proper 'f'
    segment_mapping['f'] = digit_segment_sets[1].difference({segment_mapping['c']}).pop()
    # segment_mapping.keys() == ['a', 'c', 'd', 'e', 'f']

    # The segment label in 4, that does not map to proper 'c', 'd', or 'f', is proper 'b'
    segments_cdf = { segment_mapping[x] for x in ['c', 'd', 'f'] }
    segment_mapping['b'] = digit_segment_sets[4].difference(segments_cdf).pop()
    # segment_mapping.keys() == ['a', 'b', 'c', 'd', 'e', 'f']

    # The segment in 8 that is not already mapped is proper 'g'
    segments_abcdef = { x for x in segment_mapping.values() }
    segment_mapping['g'] = digit_segment_sets[8].difference(segments_abcdef).pop()
    # segment_mapping.keys() == ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    return segment_mapping


def get_digit_segment_sets(signal_patterns):
    """Return dictionary of digits keyed to the sets of segment labels that correspond to them."""
    digit_segment_sets = {}

    segment_mapping = get_segment_mapping(signal_patterns)

    # Sets of segments that should correspond to each digit
    proper_digit_segment_sets = {
        0: {'a', 'b', 'c',      'e', 'f', 'g'},
        1: {          'c',           'f'     },
        2: {'a',      'c', 'd', 'e',      'g'},
        3: {'a',      'c', 'd',      'f', 'g'},
        4: {     'b', 'c', 'd',      'f'     },
        5: {'a', 'b',      'd',      'f', 'g'},
        6: {'a', 'b',      'd', 'e', 'f', 'g'},
        7: {'a',      'c',           'f'     },
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        9: {'a', 'b', 'c', 'd',      'f', 'g'}
    }

    # Add the mapped segment labels for each digit to the segment set for it
    for digit in proper_digit_segment_sets:
        digit_segment_sets[digit] = set()
        for proper_segment in proper_digit_segment_sets[digit]:
            digit_segment_sets[digit].add(segment_mapping[proper_segment])

    return digit_segment_sets