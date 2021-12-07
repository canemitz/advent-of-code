#! /usr/bin/python3
import importlib

# WIP: set up to use parseargs, etc., and take in which year / day / part to run
year = '2021'
day = '4'
part = '1'
example = ''
# example = '_example'

# Import solutions by day into 'days' dict
days = {}
days[day] = importlib.import_module(f'2021.day{day}')

example_str = ' (example data)' if example else ''
print(f'Getting solution for year {year}, day {day}, part {part}{example_str}...\n')

input_filepath = f'{year}/input_files/day{day}{example}.txt'
with open(input_filepath) as input_file:
    if part == '1':
        days[day].part1(input_file)
    elif part =='2':
        days[day].part2(input_file)
    else:
        raise Error(f'Part {part} does not exist')