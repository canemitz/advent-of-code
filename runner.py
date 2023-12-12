#! /usr/bin/python3

"""Run an Advent of Code solution.

Usage: ./runner.py [puzzle arguments] [solution arguments | printing arguments]
"""


import argparse
import datetime
import importlib
import json
import os
import time


def main():
    start_time = time.time()

    args = parse_args()
    year             = args.year
    day              = args.day
    part             = args.part
    alt              = args.alt
    verbose          = args.verbose
    example          = args.example
    skip_parsing     = args.skip_parsing
    print_input      = args.print_input or args.print_input_json
    print_input_json = args.print_input_json
    babn             = args.babn

    soln_str = 'solution'
    if babn:
        soln_str = f"BABN's {soln_str}"
    if alt:
        soln_str = f'alt {soln_str} {alt}'

    ex_str = ''
    if example:
        ex_str = f' (using example input{" " + example if example > 1 else ""})'

    print(f"Getting {soln_str} for year {year}, day {day}, part {part}{ex_str}...\n")

    solutions = importlib.import_module(f'{year}.day{day}{"_babn" if babn else ""}')
    solution_function = getattr(solutions, f'part{part}{f"_alt{alt}" if alt else ""}{"_verbose" if verbose else ""}')

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
            if print_input_json:
                parsed_input = json.dumps(parsed_input, indent=4)
            print(f'Puzzle input:\n{parsed_input}')
        else:
            solution_function(parsed_input)

    print_time_taken(start_time)


def parse_args():
    today = datetime.date.today()

    # Avoid insertion of linebreak between long argument names and their help strings until reaching half the terminal width (default is just 24 chars)
    MostlyRawTextHelpFormatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=int( os.get_terminal_size().columns / 2 ))

    parser = argparse.ArgumentParser(description=__doc__, add_help=True, usage=argparse.SUPPRESS, formatter_class=MostlyRawTextHelpFormatter)

    puzzle_args = parser.add_argument_group('puzzle arguments')
    puzzle_args.add_argument('-y' , '--year'        , default=today.year , help=f'AoC Year    [default: {today.year}]')
    puzzle_args.add_argument('-d' , '--day'         , default=today.day  , help=f'Puzzle day  [default: {today.day}]')
    puzzle_args.add_argument('-p' , '--part'        , default=1          , help=f'Puzzle part [default: 1]')
    puzzle_args.add_argument('-x' , '--example'     , action='count'     , help='Use example puzzle input (pass multiple times to use alternate example inputs)')

    solution_args = parser.add_argument_group('solution arguments')
    solution_args.add_argument('-a' , '--alt'         , default=0          , help='Run alternate solution function part<PART>_alt<ALT>')
    solution_args.add_argument('-v' , '--verbose'     , action='store_true', help='Run part<PART>_verbose (to print various intermediate steps)')
    solution_args.add_argument('-bn', '--babn'        , action='store_true', help="Use BABN's solution module (<YEAR>.day<DAY>_babn)")
    s_help = 'Pass file object directly to solution function\n(DEPRECATED, define custom parse_input function in the solution file instead)'
    solution_args.add_argument('-s' , '--skip-parsing', action='store_true', help=s_help)


    input_printing_args = parser.add_argument_group('printing arguments')
    input_printing_args.add_argument('-pr', '--print-input'     , action='store_true', help='Print parsed puzzle input instead of calling solution function')
    input_printing_args.add_argument('-pj', '--print-input-json', action='store_true', help='Print parsed puzzle input as json instead of calling solution function (helpful for dictionary-like inputs)')

    return parser.parse_args()

def parse_input(input_file_obj):
    return input_file_obj.read().strip().split('\n')


def print_time_taken(start_time):
    total_duration_seconds = time.time() - start_time

    (hours, minutes_remaining) = divmod(total_duration_seconds, 3600)
    (minutes, seconds) = divmod(minutes_remaining, 60)

    duration_arr = []
    decimals = 3
    if minutes:
        duration_arr.append(f'{int(minutes)}m')
        decimals = 2
    if hours:
        duration_arr.insert(0, f'{int(hours)}h')
        decimals = 0
    if decimals:
        factor = 10**decimals
        seconds = round(seconds*factor) / factor
        seconds_split = str(float(seconds)).split('.')
        seconds = seconds_split[0] + '.' + seconds_split[1].ljust(decimals, '0')
    else:
        seconds = round(seconds)
    duration_arr.append(f'{seconds}s')

    duration_str = ' '.join(duration_arr)

    print(f'\n(solution duration {duration_str})')


if __name__ == '__main__':
    main()
