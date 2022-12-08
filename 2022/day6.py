def part1(puzzle_input):
    print('Q: How many characters need to be processed before the first start-of-packet marker is detected?')

    signal = puzzle_input[0]
    start_of_packet_marker_length = 4

    ans = find_final_index_of_marker(signal, start_of_packet_marker_length) + 1

    print(f'A: {ans}')


def find_final_index_of_marker(signal, marker_length):
    """Return index of the final character of a marker in a signal, where a marker is a sequence of non-repeating characters of a certain length"""
    marker = []
    for i in range(len(signal)):

        # Remove oldest character
        if len(marker) == marker_length:
            marker.pop(0)

        # Add new character
        char = signal[i]
        marker.append(char)

        # Check current set of characters for uniqueness
        if len(set(marker)) == marker_length:
            return i


def part2(puzzle_input):
    print('Q: How many characters need to be processed before the first start-of-message marker is detected?')

    signal = puzzle_input[0]
    start_of_message_marker_length = 14

    ans = find_final_index_of_marker(signal, start_of_message_marker_length) + 1

    print(f'A: {ans}')