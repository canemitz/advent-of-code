import numpy as np


def part1(octopus_energy_levels):
    print('Q: How many total flashes are there after 100 steps?')
    octopus_arr = get_octopus_arr(octopus_energy_levels)

    total_flashes = 0
    for n in range(100):
        (octopus_arr, num_flashes) = take_a_step(octopus_arr)
        total_flashes += num_flashes

    print(f'A: {total_flashes}')


def get_octopus_arr(octopus_energy_levels):
    octopus_lol = []

    for line in octopus_energy_levels.readlines():
        row = [int(x) for x in line if x != '\n']
        octopus_lol.append(row)

    octopus_arr = np.array(octopus_lol)
    return octopus_arr


def take_a_step(octopus_arr):
    # Increment all energy levels
    octopus_arr += 1

    # Any octopus with energy level > 9 flash
    octopus_who_flashed = []
    for octopus in zip(*np.where(octopus_arr == 10)):
        if octopus not in octopus_who_flashed:
            (octopus_arr, octopus_who_flashed) = octopus_flashes(octopus_arr, octopus, octopus_who_flashed)

    # Reset energy levels of all octopus who flashed
    for octopus in octopus_who_flashed:
        octopus_arr[octopus] = 0

    return octopus_arr, len(octopus_who_flashed)


def octopus_flashes(octopus_arr, octopus, octopus_who_flashed):
    octopus_who_flashed.append(octopus)
    octo_neighbors = get_octo_neighbor_coords(octopus_arr, octopus)

    # Increment energy level of all octo-neighbors, unless they've already flashed this step
    for octo_neighbor in octo_neighbors:
        if octo_neighbor not in octopus_who_flashed:
            octopus_arr[octo_neighbor] += 1
            if octopus_arr[octo_neighbor] == 10:
                (octopus_arr, octopus_who_flashed) = octopus_flashes(octopus_arr, octo_neighbor, octopus_who_flashed)

    return octopus_arr, octopus_who_flashed


def get_octo_neighbor_coords(arr, coord):
    """Return list of coords of octo neighbors that exist."""
    (y0, x0) = coord
    (y_max, x_max) = arr.shape

    neighbor_coords = []

    for y in [y0-1, y0, y0+1]:
        for x in [x0-1, x0, x0+1]:
            neighbor_coord = (y, x)
            if (-1 < y < y_max) and (-1 < x < x_max) and (neighbor_coord != coord):
                neighbor_coords.append(neighbor_coord)

    return neighbor_coords


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')