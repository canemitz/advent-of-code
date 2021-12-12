import math
import numpy as np

def part1(heightmap):
    print('Q: What is the sum of the risk levels of all low points on your heightmap?')

    heightmap_arr = get_heightmap_arr(heightmap)

    low_point_coords = get_low_point_coords(heightmap_arr)
    low_point_risk_levels = [int(heightmap_arr[coord])+1 for coord in low_point_coords]

    ans = sum(low_point_risk_levels)
    print(f'A: {ans}')


def get_heightmap_arr(heightmap):
    heightmap_lol = []

    for line in heightmap.readlines():
        row = [x for x in line if x != '\n']
        heightmap_lol.append(row)

    heightmap_arr = np.array(heightmap_lol)
    return heightmap_arr


def get_low_point_coords(heightmap_arr):
    low_point_coords = []

    (y_max, x_max) = heightmap_arr.shape

    for y in range(y_max):
        for x in range(x_max):
            val = int(heightmap_arr[y, x])

            low_point = True

            if x > 0:
                left = int(heightmap_arr[y, x-1])
                if val >= left:
                    low_point = False
            if x < x_max-1:
                right = int(heightmap_arr[y, x+1])
                if val >= right:
                    low_point = False
            if y > 0:
                up = int(heightmap_arr[y-1, x])
                if val >= up:
                    low_point = False
            if y < y_max-1:
                down = int(heightmap_arr[y+1, x])
                if val >= down:
                    low_point = False

            if low_point:
                low_point_coords.append((y, x))

    return low_point_coords


def part2(heightmap):
    print('Q: What do you get if you multiply together the sizes of the three largest basins?')

    heightmap_arr = get_heightmap_arr(heightmap)
    basins = get_basins(heightmap_arr)

    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort(reverse=True)
    largest_three_basin_sizes = [basin_sizes[x] for x in range(3)]

    ans = math.prod(largest_three_basin_sizes)
    print(f'A: {ans}')


def get_basins(heightmap_arr):
    """Return list of basins containing sets of coords in each basin."""
    low_point_coords = get_low_point_coords(heightmap_arr)
    basins = []
    coords_already_checked = {coord for coord in low_point_coords}

    # For each low point, check its neighbors to see if they're also in the basin (not a 9, or edge of board)
    for low_point in low_point_coords:
        basin = {low_point}
        (basin, coords_already_checked) = expand_basin(heightmap_arr, basin, low_point, coords_already_checked)
        basins.append(basin)

    return basins


def expand_basin(heightmap_arr, basin, coord, coords_already_checked):
    """Recursively add neighbors of this coord to this basin if they belong.
    Return basin and list of coords already checked (to avoid neighbors checking neighbors ad infinitum).
    """
    (y_max, x_max) = heightmap_arr.shape
    (y0, x0) = coord

    # Get neighbor elements that exist
    neighbors = []
    for y in [y0-1, y0+1]:
        neighbor_coord = (y, x0)
        if (-1 < y < y_max) and (neighbor_coord not in coords_already_checked):
            neighbors.append(neighbor_coord)
        coords_already_checked.add(neighbor_coord)
    for x in [x0-1, x0+1]:
        neighbor_coord = (y0, x)
        if (-1 < x < x_max) and (neighbor_coord not in coords_already_checked):
            neighbors.append(neighbor_coord)
        coords_already_checked.add(neighbor_coord)

    # Add neighbors to this basin
    for neighbor_coord in neighbors:
        neighbor_val = int(heightmap_arr[neighbor_coord])
        if neighbor_val < 9:
            basin.add(neighbor_coord)
            (basin, coords_already_checked) = expand_basin(heightmap_arr, basin, neighbor_coord, coords_already_checked)

    return basin, coords_already_checked