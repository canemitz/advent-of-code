#! /usr/bin/python3

"""Run an Advent of Code solution.
"""


import argparse
import datetime
import importlib
import json
import time


def main():
    start_time = time.time()

    args = parse_args()
    year         = args.year
    day          = args.day
    part         = args.part
    verbose      = args.verbose
    example      = args.example
    skip_parsing = args.skip_parsing
    print_input  = args.print_input
    print_json   = args.json

    print(f"Getting solution for year {year}, day {day}, part {part}{' (using example input)' if example else ''}...\n")

    solutions = importlib.import_module(f'{year}.day{day}')
    solution_function = getattr(solutions, f'part{part}{"_verbose" if verbose else ""}')

    example_str = ''
    if example:
        example_str = '_example'
        if example > 1:
            example_str += str(example)

    input_filepath = f"{year}/input_files/day{day}{example_str}.txt"
    with open(input_filepath) as input_file:
        try:
            parse_input_function = solutions.parse_input
        except:
            parse_input_function = parse_input

        if skip_parsing:
            parsed_input = input_file
        else:
            parsed_input = parse_input_function(input_file)

        if print_input:
            if print_json:
                parsed_input = json.dumps(parsed_input, indent=4)
            print(f'Puzzle input:\n{parsed_input}')
        else:
            solution_function(parsed_input)

    print_time_taken(start_time)


def parse_args():
    today = datetime.date.today()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-y', '--year', default=today.year)
    parser.add_argument('-d', '--day',  default=today.day)
    parser.add_argument('-p', '--part', default=1)
    parser.add_argument('-x', '--example', action='count', help='Use example puzzle input (pass multiple times to use alternate example inputs)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print output for comparison with example')
    parser.add_argument('-s', '--skip-parsing', action='store_true', help='Pass file object directly to solution function')
    parser.add_argument('-pr', '--print-input', action='store_true', help='Print parsed puzzle input instead of calling solution function')
    parser.add_argument('-j', '--json', action='store_true', help='Print parsed puzzle input as json (helpful for dictionary-like inputs)')

    return parser.parse_args()


def parse_input(input_file_obj):
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
