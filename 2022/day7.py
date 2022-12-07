from functools import reduce
import operator
import re


cd_regex = re.compile(r'^\$ cd (.+)')
ls_regex = re.compile(r'^\$ ls')
dir_regex  = re.compile(r'^dir (.+)')
file_regex = re.compile(r'^(\d+) (.+)')
cd_up_regex = re.compile(r'^\.\.$')


def part1(puzzle_input):
    print('Q: Find all of the directories with a total size of at most 100,000. What is the sum of the total sizes of those directories?')

    fs = build_fs_dict(puzzle_input)
    dir_sizes, _ = get_size_of_dir(fs['/'])

    ans = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100000:
            ans += dir_size

    print(f'A: {ans}')


def get_size_of_dir(dir_, pwd = [], dir_sizes = {}):
    """Get the total size of the contents of a dir, and return updated dictionary of all dir sizes keyed by path."""
    dir_size = 0
    for item_name, item_value in dir_.items():
        if type(item_value) is dict:
            subdir = pwd + [item_name]
            dir_sizes, subdir_size = get_size_of_dir(item_value, subdir, dir_sizes )
            dir_size += subdir_size
        else:
            dir_size += int(item_value)

    dir_path = '/' + '/'.join(pwd)
    dir_sizes[dir_path] = dir_size

    return dir_sizes, dir_size


def build_fs_dict(puzzle_input):
    """Using cd and ls commands, build a nested dictionary representing the file system."""
    pwd = []
    fs = {}

    for line in puzzle_input:
        if cd_match := cd_regex.match(line):
            (fs, pwd) = cd_dir(fs, pwd, cd_match.group(1))
        elif ls_regex.match(line):
            pass
        elif ls_dir_match := dir_regex.match(line):
            fs = ls_dir(fs, pwd, ls_dir_match.group(1))
        elif ls_file_match := file_regex.match(line):
            fs = ls_file(fs, pwd, ls_file_match.group(2), ls_file_match.group(1))

    return fs


def ls_dir(fs, pwd, dir_name=None):
    """Ensure dir exists in fs."""
    dir_path = pwd + [dir_name] if dir_name else pwd
    try:
        get_from_dict(fs, dir_path)
    except KeyError:
        set_in_dict(fs, dir_path, {})

    return fs


def ls_file(fs, pwd, file_name, size):
    """Set file size in fs at pwd."""
    file_path = pwd + [file_name]
    set_in_dict(fs, file_path, size)
    return fs


def cd_dir(fs, pwd, new_dir):
    """Update pwd, and ensure dir exists in fs."""
    if cd_up_regex.match(new_dir):
        pwd = pwd[:-1]
    else:
        pwd.append(new_dir)

    fs = ls_dir(fs, pwd)

    return fs, pwd


def get_from_dict(dict_, keys_list):
    """Get nested value."""
    return reduce(operator.getitem, keys_list, dict_)


def set_in_dict(dict_, keys_list, value):
    """Set nested value."""
    get_from_dict(dict_, keys_list[:-1])[keys_list[-1]] = value


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')