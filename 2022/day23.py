import numpy as np


def part1(puzzle_input):
    print("Q: Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds.")
    print("   How many empty ground tiles does that rectangle contain?")

    grove_map = puzzle_input

    for round_i in range(10):
        grove_map = pad_grove_map(grove_map)
        proposed_moves = consider_and_propose_moves(grove_map, round_i)
        grove_map = elves_move(grove_map, proposed_moves)
        grove_map = prune_grove_map(grove_map)

    ans = len(np.where(grove_map == '.')[0])

    print(f'A: {ans}')


def consider_and_propose_moves(grove_map, round_i):
    """Return coordinates of proposed destinations keyed to current coordinates of elves that want to move there."""
    proposed_moves = {}

    elf_coords = zip( *np.where(grove_map == '#') )
    for elf_coord in elf_coords:
        proposed_move = propose_move(grove_map, elf_coord, round_i)
        if proposed_move:
            try:
                proposed_moves[repr(proposed_move)] += [elf_coord]
            except:
                proposed_moves[repr(proposed_move)] = [elf_coord]

    return proposed_moves


def propose_move(grove_map, elf_coord, round_i):
    elf_y, elf_x = elf_coord

    N = (elf_y - 1, elf_x)
    S = (elf_y + 1, elf_x)
    E = (elf_y, elf_x + 1)
    W = (elf_y, elf_x - 1)

    NE = (elf_y - 1, elf_x + 1)
    NW = (elf_y - 1, elf_x - 1)
    SE = (elf_y + 1, elf_x + 1)
    SW = (elf_y + 1, elf_x - 1)

    coords_to_check = {
        'N': [ N, NE, NW ],
        'S': [ S, SE, SW ],
        'W': [ W, NW, SW ],
        'E': [ E, NE, SE ]
    }

    directions = ['N', 'S', 'W', 'E']
    round_mod_4 = round_i % 4
    directions_ordered = directions[round_mod_4:] + directions[:round_mod_4]

    proposed_move = None
    for direction in directions_ordered:
        coords = tuple(zip(*coords_to_check[direction]))
        if np.all(grove_map[ coords ] == '.'):
            proposed_move = eval(direction)
            break

    return proposed_move


def elves_move(grove_map, proposed_moves):
    for new_coord, elf_coords in proposed_moves.items():
        if len(elf_coords) == 1:
            grove_map[elf_coords[0]] = '.'
            grove_map[eval(new_coord)]  = '#'

    return grove_map


def prune_grove_map(grove_map):
    """Remove outer-most rows and columns that only contain ground."""
    while np.all(grove_map[0, :]  == '.'):
        grove_map = np.delete(grove_map,  0,  0)
    while np.all(grove_map[-1, :] == '.'):
        grove_map = np.delete(grove_map, -1,  0)
    while np.all(grove_map[:, 0]  == '.'):
        grove_map = np.delete(grove_map,  0, -1)
    while np.all(grove_map[:, -1] == '.'):
        grove_map = np.delete(grove_map,  -1, -1)

    return grove_map


def pad_grove_map(grove_map):
    """Add a border of ground around the current map."""
    grove_map_padded = np.pad(grove_map, pad_width=1, mode='constant', constant_values='.')
    return grove_map_padded


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')


def parse_input(input_file_obj):
    """Return numpy array with one character per element."""
    input_list = input_file_obj.read().strip().split('\n')

    puzzle_input = np.array([ [char for char in row] for row in input_list ])

    return puzzle_input