def part1(puzzle_input):
    print('Q: Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.')
    print('   What is the sum of these six signal strengths?')

    signal_strengths = []
    cycle = 0
    X = 1
    busy = 0
    pending_add = 0

    while puzzle_input:
        cycle += 1

        # Calculate signal strength on the 20th cycle, and every 40 after that
        if (cycle - 20) % 40 == 0:
            signal_strength = cycle*X;
            signal_strengths.append(signal_strength)

        if not busy:
            # Get next instruction
            line = puzzle_input.pop(0)
            try:
                # addx
                command, pending_add = line.split()
                busy = 2
            except:
                # noop
                command = line

        if busy:
            busy -= 1

        if not busy and pending_add:
            X += int(pending_add)
            pending_add = 0

    ans = sum(signal_strengths)

    print(f'A: {ans}')


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')