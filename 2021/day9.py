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
    print('Q:')
    print(f'A: {ans}')