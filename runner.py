#! /usr/bin/python3
import importlib

# WIP: set up to use parseargs, etc., and take in which year / day / part to run
year = '2021'
day = '1'
part = '2'

# Import solutions by day into 'days' dict
days = {}
days[day] = importlib.import_module(f'2021.day{day}')

print(f'Getting solution for year {year}, day {day}, part {part}...\n')

input_filepath = f'{year}/input_files/day{day}.txt'
with open(input_filepath) as input_file:
    if part == '1':
        days[day].part1(input_file)
    elif part =='2':
        days[day].part2(input_file)
    else:
        raise Error(f'Part {part} does not exist')