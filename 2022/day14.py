import numpy as np


def part1(puzzle_input):
    print('Q: Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?')

    rock_map = get_initial_rock_map(puzzle_input)
    sand_src_y = 0
    sand_src_x = 500
    rock_map[sand_src_y, sand_src_x] = '+'

    # Drop sand grains until the map doesn't change
    num_sand_grains = 0
    prev_rock_map = np.array([])
    while not np.array_equal(rock_map, prev_rock_map):
        prev_rock_map = np.copy(rock_map)
        rock_map = drop_sand_grain(rock_map, sand_src_y, sand_src_x)
        num_sand_grains += 1

    ans = num_sand_grains - 1

    print(f'A: {ans}')


def get_initial_rock_map(puzzle_input):
    """Find necessary size of rock map so we don't have to dynamically change it.
       (which might be better, but this is simpler when I'm forgetful with numpy)
    """
    max_x = 1
    max_y = 1

    # Looping over the puzzle input twice is unnecessary, but simpler, and it works
    for rock_path in puzzle_input:
        for point in rock_path.split(' -> '):
            [x, y] = [ int(coord) for coord in point.split(',') ]
            max_x = max(x+1, max_x)
            max_y = max(y+1, max_x)

    # Create rock_map array big enough to hold all coords, filled with air
    rock_map = np.full([max_y, max_x], '.', dtype=str)

    # Each line is a separate path of rock
    for rock_path in puzzle_input:
        # Create list holding points of this rock path
        points = []
        for point in rock_path.split(' -> '):
            points.append([ int(x) for x in point.split(',') ])

        # Draw a rock line between each point and the next
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]

            # Add 1 for easy indexing/slicing
            x_max = max(p1[0], p2[0]) + 1
            y_max = max(p1[1], p2[1]) + 1
            x_min = min(p1[0], p2[0])
            y_min = min(p1[1], p2[1])

            # Add rock along this line
            rock_map[ y_min:y_max, x_min:x_max ] = '#'

    return rock_map


def drop_sand_grain(rock_map, sand_y, sand_x):
    """Determine the next position of a grain of sand experiencing gravity. Return once it settles or falls into the abyss."""

    # Get contents of units at possible next positions if they exist
    try:
        unit_down = rock_map[sand_y+1, sand_x]
    except:
        unit_down = None
    try:
        unit_down_left  = rock_map[sand_y+1, sand_x-1]
    except:
        unit_down_left = None
    try:
        unit_down_right = rock_map[sand_y+1, sand_x+1]
    except:
        unit_down_right = None

    if not unit_down:
        # Falls into the abyss
        pass
    elif unit_down == '.':
        # Drop sand grain directly below
        rock_map = drop_sand_grain(rock_map, sand_y+1, sand_x)
    elif not unit_down_left:
        # Falls into the abyss
        pass
    elif unit_down_left == '.':
        # Drop sand grain down and to the left
        rock_map = drop_sand_grain(rock_map, sand_y+1, sand_x-1)
    elif not unit_down_right:
        # Falls into the abyss
        pass
    elif unit_down_right == '.':
        # Drop sand grain down and to the right
        rock_map = drop_sand_grain(rock_map, sand_y+1, sand_x+1)
    else:
        # Otherwise, sand grain is at rest
        rock_map[sand_y, sand_x] = 'o'

    return rock_map


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')