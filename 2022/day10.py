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
    print('Q: Render the image given by your program. What eight capital letters appear on your CRT?')

    crt_width  = 40
    crt_height = 6
    num_pixels = crt_width * crt_height

    # Position of center sprite pixel
    X = 1
    sprite_width = 3
    sprite_offset = (sprite_width - 1) / 2
    busy = 0
    pending_add = 0
    row_i = 0

    ans = ''
    for pixel_i in range(num_pixels):
        # Move to next row after end of line
        try:
            if cycle % crt_width == 0:
                row_i += 1
                ans += '\n'
        except:
            pass

        cycle = pixel_i + 1

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

        pixel = ' '
        if (X - sprite_offset) <= (pixel_i - (crt_width*row_i)) <= (X + sprite_offset):
            pixel = '█'
        ans += pixel

        if busy:
            busy -= 1

        if not busy and pending_add:
            X += int(pending_add)
            pending_add = 0

    print(f'A: \n{ans}')


def part2_debug(puzzle_input):
    """Copy of part2, but pauses after each cycle, and prints out information as in Eric's example for easy comparison."""
    print('Q: Render the image given by your program. What eight capital letters appear on your CRT?')

    crt_width  = 40
    crt_height = 6
    num_pixels = crt_width * crt_height

    # Position of center sprite pixel
    X = 1
    sprite_width = 3
    sprite_offset = (sprite_width - 1) / 2
    busy = 0
    pending_add = 0
    row_i = 0

    ans = ''
    for pixel_i in range(num_pixels):
        # Move to next row after end of line
        try:
            if cycle % crt_width == 0:
                row_i += 1
                ans += '\n'
        except:
            pass

        cycle = pixel_i + 1

        if not busy:
            # Get next instruction
            line = puzzle_input.pop(0)
            try:
                # addx
                command, pending_add = line.split()
                busy = 2
                print(f'Start cycle {str(cycle).rjust(3)}: begin executing {command} {pending_add}')
            except:
                # noop
                command = line
                print(f'Start cycle {str(cycle).rjust(3)}: begin executing {command}')

        pixel = '.'

        if (X - sprite_offset) <= (pixel_i - (crt_width*row_i)) <= (X + sprite_offset):
            pixel = '#'
        ans += pixel
        print(f'During cycle {str(cycle).rjust(2)}: CRT draws pixel in position {pixel_i}')

        current_crt_row = ans.split('\n').pop()
        print(f'Current CRT row: {current_crt_row}')

        if busy:
            busy -= 1

        if not busy and pending_add:
            X += int(pending_add)
            print(f'End of cycle {str(cycle).rjust(1)}: finish executing addx {pending_add} (Register X is now {X})')
            pending_add = 0
            sprite_position = ['.' for x in range(X-1) ]
            sprite_position += ['###']
            sprite_position += ['.' for x in range (X+1, crt_width)]
            print(f'Sprite position: {"".join(sprite_position)}')
        elif not busy:
            print(f'End of cycle {str(cycle).rjust(1)}: finish executing noop')

        input()

    print(f'A: \n{ans}')