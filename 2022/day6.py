def part1(puzzle_input):
    print('Q: How many characters need to be processed before the first start-of-packet marker is detected?')

    signal = puzzle_input[0]
    start_of_packet_marker = []

    chars_processed = 0
    for i in range(len(signal)):

        # Remove oldest character
        if len(start_of_packet_marker) == 4:
            start_of_packet_marker.pop(0)

        # Add new character
        char = signal[i]
        start_of_packet_marker.append(char)

        # Check current set of characters for uniqueness
        if len(set(start_of_packet_marker)) == 4:
            chars_processed = i+1
            break

    ans = chars_processed

    print(f'A: {ans}')


def part2(puzzle_input):
    print('Q:')


    print(f'A: {ans}')