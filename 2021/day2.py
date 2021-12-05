def part1(input_data):
    print('Q: What do you get if you multiply your final horizontal position by your final depth?')

    horizontal = 0
    vertical = 0

    for command in input_data:
        (direction, value) = command.split(' ')
        
        if direction == 'forward':
            horizontal += int(value)
        elif direction == 'down':
            vertical += int(value)
        elif direction == 'up':
            vertical -= int(value)

    ans = horizontal * vertical
    print(f'A: {ans}')


def part2(input_data):
    print('Q: What do you get if you multiply your final horizontal position by your final depth?')

    aim = 0
    horizontal = 0
    vertical = 0

    for command in input_data:
        (direction, value) = command.split(' ')
        
        if direction == 'forward':
            horizontal += int(value)
            vertical += aim*int(value)
        elif direction == 'down':
            aim += int(value)
        elif direction == 'up':
            aim -= int(value)

    ans = horizontal * vertical
    print(f'A: {ans}')