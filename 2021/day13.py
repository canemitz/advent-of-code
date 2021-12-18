import math
import numpy as np


def part1(transparent_paper):
    print('Q: How many dots are visible after completing just the first fold instruction on your transparent paper?')

    dots_arr, folding_instructions = parse_transparent_paper_input(transparent_paper)

    dots_arr_folded = dots_arr
    for i in range(1):
        dots_arr_folded = fold_along(folding_instructions[i], dots_arr_folded)

    (dot_rows, dot_cols) = np.where(dots_arr_folded > 0)
    num_dots_visible = len(dot_rows)

    print(f'A: {num_dots_visible}')


def parse_transparent_paper_input(transparent_paper):
    dot_coords = []
    folding_instructions = []

    for line in transparent_paper.readlines():
        line_split = line.split('fold along ')

        # Grab either the coordinate or the folding instruction
        line_val = line_split[-1].strip()
        if len(line_split) == 2:
            folding_instructions.append(line_val)
        elif len(line_val):
            dot_coords.append(line_val)

    dots_arr = get_dots_arr(dot_coords)

    return dots_arr, folding_instructions


def get_dots_arr(dot_coords):
    y_max = 0
    x_max = 0

    # list to hold coordinates using numpy notation of y,x (instead of x,y)
    np_coords = []

    # Figure out how big the array needs to be, and populate np_coords
    for coord in dot_coords:
        x, y = coord.split(',')
        y = int(y)
        x = int(x)
        y_max = max(y, y_max)
        x_max = max(x, x_max)
        np_coords.append((y, x))

    # Create array of zeros, with ones where dots are
    dots_arr = np.zeros([y_max+1, x_max+1], dtype=int)
    for coord in np_coords:
        dots_arr[coord] = 1

    return dots_arr


def fold_along(fold_line, dots_arr):
    axis, fold_val = fold_line.split('=')

    fold_val = int(fold_val)

    (y_max, x_max) = dots_arr.shape

    # y means horizontal line, which is along the 0 axis for numpy
    if axis == 'y':
        # Separate top and bottom parts
        top_part = dots_arr[:fold_val]
        bottom_part_flipped = np.flip(dots_arr[fold_val+1:], axis=0)

        # Add columns of zeroes as needed to make the parts match in shape
        (top_y_max, _)    = top_part.shape
        (bottom_y_max, _) = bottom_part_flipped.shape
        y_diff = top_y_max - bottom_y_max
        padding = np.zeros((y_diff, x_max))

        if y_diff > 0:
            bottom_part_flipped = np.vstack((padding, bottom_part_flipped))
        elif y_diff < 0:
            top_part = np.vstack((padding, top_part))

        # Overlap the top and bottom parts
        dots_arr_folded = top_part + bottom_part_flipped

    else:
        # Separate left and right parts
        left_part = dots_arr[:, :fold_val]
        right_part_flipped = np.flip(dots_arr[:, fold_val+1:], axis=1)

        # Add rows of zeroes as needed to make the parts match in shape
        (_, left_x_max)    = left_part.shape
        (_, right_x_max) = right_part_flipped.shape
        x_diff = left_x_max - right_x_max
        padding = np.zeros((y_max, x_diff))

        if x_diff > 0:
            right_part_flipped = np.hstack((padding, right_part_flipped))
        elif x_diff < 0:
            left_part = np.hstack((padding, left_part))

        # Overlap left and right parts
        dots_arr_folded = left_part + right_part_flipped

    return dots_arr_folded


def part2(transparent_paper):
    print('Q: What code do you use to activate the infrared thermal imaging camera system?')

    dots_arr, folding_instructions = parse_transparent_paper_input(transparent_paper)

    dots_arr_folded = dots_arr
    for folding_instruction in folding_instructions:
        dots_arr_folded = fold_along(folding_instruction, dots_arr_folded)

    # Print out folded dots array in a readable manner
    arr_to_print = dots_arr_folded.astype(str)
    arr_to_print[dots_arr_folded > 0] = '██'
    arr_to_print[dots_arr_folded == 0] = '  '
    arr_to_print_str = '\n'.join( [''.join(row) for row in arr_to_print] )

    print(f'A:\n\n{arr_to_print_str}\n')