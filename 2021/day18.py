import itertools
import math
import re

def part1(homework_assignment):
    print('Q: Add up all of the snailfish numbers from the homework assignment in the order they appear.')
    print('What is the magnitude of the final sum?')

    final_sum = ''
    for snailfish_number in homework_assignment.readlines():
        final_sum = add_numbers(final_sum, snailfish_number.strip())

    ans = get_magnitude(final_sum)

    print(f'\nA: {ans}')


def add_numbers(a, b):
    if a and b:
        numbers_added = reduce_number_fully(f'[{a},{b}]')
    elif a:
        numbers_added = reduce_number_fully(a)
    elif b:
        numbers_added = reduce_number_fully(b)

    return numbers_added


def reduce_number_fully(num):
    num_prev = num
    num_reduced = reduce_number(num)

    while num_reduced != num_prev:
        num_prev = num_reduced
        num_reduced = reduce_number(num_prev)

    return num_reduced


def reduce_number(num):
    if not num:
        return ''

    num_exploded = explode_number(num)

    num_reduced = split_number_once(num_exploded)
    while num_reduced != num_exploded:
        num_exploded = explode_number(num_reduced)
        num_reduced = split_number_once(num_exploded)

    return num_reduced


def explode_number(num):
    num_exploded = num

    pair_to_explode_idx = get_pair_to_explode(num)
    while pair_to_explode_idx:
        num_exploded = explode_pair_in_num(pair_to_explode_idx, num_exploded)
        pair_to_explode_idx = get_pair_to_explode(num_exploded)

    return num_exploded


def explode_pair_in_num(pair_idx, num):
    pair = num[pair_idx[0]:pair_idx[1]]
    (x, y) = pair.split(',')
    x = x[1:]
    y = y[:-1]

    left = num[:pair_idx[0]]
    right = num[pair_idx[1]:]

    nums_left = re.findall(r'\d+', left)
    left_new = left
    if nums_left:
        first_num_left = nums_left[-1]
        new_num_left = str(int(first_num_left) + int(x))
        new_num_left_reversed = new_num_left[::-1]

        left_reversed = left[::-1]
        left_new = re.sub(first_num_left[::-1], new_num_left_reversed, left_reversed, 1)[::-1]

    nums_right = re.findall(r'\d+', right)
    right_new = right
    if nums_right:
        first_num_right = nums_right[0]
        new_num_right = str(int(first_num_right) + int(y))
        right_new = re.sub(first_num_right, new_num_right, right, 1)

    num_exploded = left_new + '0' + right_new
    return num_exploded


def split_number_once(num):
    nums_over_10 = re.findall(r'\d{2}', num)

    num_split = num
    if nums_over_10:
        num_splitting = nums_over_10[0]
        x = math.floor(float(num_splitting) / 2)
        y = math.ceil(float(num_splitting) / 2)
        (left, right) = num.split(nums_over_10[0], 1)
        num_split = left + f'[{x},{y}]' + right

    return num_split


def get_pair_to_explode(num):
    """Return index of first pair nested inside four pairs."""
    pair_to_explode_idx = None
    regular_number_pair_regex = r'(\[\d+,\d+\])'
    regular_number_pairs = re.finditer(regular_number_pair_regex, num)

    for pair_match in regular_number_pairs:
        left = num[:pair_match.start(1)]

        num_open_brackets  = len(re.findall(r'\[', left))
        num_close_brackets = len(re.findall(r'\]', left))

        if (num_open_brackets - num_close_brackets) >= 4:
            pair_to_explode_idx = pair_match.span(1)
            break

    return pair_to_explode_idx


def get_magnitude(num):
    # The magnitude of a pair is 3 times the magnitude of its left element plus 2 times the magnitude of its right element.
    magnitude = num
    pair_regex = r'\[(\d+),(\d+)\]'

    while '[' in magnitude:
        magnitude = re.sub(pair_regex, get_magnitude_of_pair, magnitude)

    return magnitude


def get_magnitude_of_pair(match):
    x = match.group(1)
    y = match.group(2)
    magnitude = 3*int(x) + 2*int(y)
    return str(magnitude)


def part2(homework_assignment):
    print('Q: What is the largest magnitude of any sum of two different snailfish numbers from the homework assignment?')

    homework_assignment_arr = []
    for line in homework_assignment.readlines():
        homework_assignment_arr.append(line.strip())

    number_pairs = get_all_possible_pairs(homework_assignment_arr)

    largest_magnitude = 0
    for pair in number_pairs:
        pair_summed = add_numbers(pair[0], pair[1])
        magnitude = int(get_magnitude(pair_summed))
        if magnitude > largest_magnitude:
            largest_magnitude = magnitude

    print(f'\nA: {largest_magnitude}')


def get_all_possible_pairs(list_):
    all_pairs = set()
    for pair in itertools.combinations(list_, 2):
        all_pairs.add(pair)

    list_.reverse()
    for pair in itertools.combinations(list_, 2):
        all_pairs.add(pair)

    return list(all_pairs)