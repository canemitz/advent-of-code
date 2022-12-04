#! /usr/bin/python3

"""Run an Advent of Code solution.
"""


import argparse
import datetime
import importlib
import time


def main():
    start_time = time.time()

    args = parse_args()
    year         = args.year
    day          = args.day
    part         = args.part
    example      = args.example
    skip_parsing = args.skip_parsing

    print(f"Getting solution for year {year}, day {day}, part {part}{' (using example input)' if example else ''}...\n")

    solutions = importlib.import_module(f'{year}.day{day}')
    solution_function = getattr(solutions, f'part{part}')

    input_filepath = f"{year}/input_files/day{day}{'_example' if example else ''}.txt"
    with open(input_filepath) as input_file:
        parsed_input = parse_input(input_file, skip_parsing)
        solution_function(parsed_input)

    print_time_taken(start_time)


def parse_args():
    today = datetime.date.today()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-y', '--year', default=today.year)
    parser.add_argument('-d', '--day',  default=today.day)
    parser.add_argument('-p', '--part', default=1)
    parser.add_argument('-x', '--example', action='store_true', help='Use example puzzle input')
    parser.add_argument('-s', '--skip-parsing', action='store_true', help='Pass file object directly to solution function')

    return parser.parse_args()


def parse_input(input_file_obj, skip_parsing):
    if skip_parsing:
        return input_file_obj
    else:
        return input_file_obj.read().strip().split('\n')


def print_time_taken(start_time):
    total_duration_seconds = round(time.time() - start_time)

    (hours, minutes_remaining) = divmod(total_duration_seconds, 3600)
    (minutes, seconds) = divmod(minutes_remaining, 60)

    duration_str = ''
    if hours:
        duration_str += f' {hours}h'
    if hours or minutes:
        duration_str += f' {minutes}m'
    if hours or minutes or seconds:
        duration_str += f' {seconds}s'
    else:
        duration_str = ' less than 1s'

    print(f'\n(solution duration{duration_str})')


if __name__ == '__main__':
    main()
