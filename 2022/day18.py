def part1(puzzle_input):
    print('Q: What is the surface area of your scanned lava droplet?')
    cubes = puzzle_input

    surface_area = 6 * len(cubes)
    for cube in cubes:
        surface_area -= num_cubes_adjacent(cube, cubes)
    ans = surface_area

    print(f'A: {ans}')


def num_cubes_adjacent(cube, cubes):
    num_cubes_adjacent = 0

    for test_cube in cubes:
        if test_cube[:2] == cube[:2] and abs(test_cube[2] - cube[2]) == 1:
            num_cubes_adjacent += 1
        elif test_cube[1:3] == cube[1:3] and abs(test_cube[0] - cube[0]) == 1:
            num_cubes_adjacent += 1
        elif [test_cube[0], test_cube[2]] == [cube[0], cube[2]] and abs(test_cube[1] - cube[1]) == 1:
            num_cubes_adjacent += 1

        if num_cubes_adjacent == 6:
            break

    return num_cubes_adjacent


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')


def parse_input(input_file_obj):
    input_lines = input_file_obj.read().strip().split('\n')

    puzzle_input = [ [int(coord) for coord in cube.split(',')] for cube in input_lines ]
    return puzzle_input