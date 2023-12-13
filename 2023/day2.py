import re


def part1(game_record):
    print('Q: Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?')

    num_cubes = {
        'red'  : 12,
        'green': 13,
        'blue' : 14
    }
    colors = num_cubes.keys()

    possible_game_ids = []
    for game_id, samples in game_record.items():
        valid_game = True
        for sample in samples:
            valid_game &= all([ sample[color] <= num_cubes[color] for color in colors ])
            if not valid_game:
                break

        if valid_game:
            possible_game_ids.append(int(game_id))

    ans = sum(possible_game_ids)

    print(f'A: {ans}')


def part2(game_record):
    print('Q:')



    print(f'A: {ans}')


def parse_input(input_file_obj):
    """Return game record as dict of games keyed by id, with list of dicts of numbers of cube color samples for each game.
    """
    game_record = {}

    puzzle_lines = input_file_obj.read().strip().split('\n')
    for line in puzzle_lines:
        (game_label, game) = line.split(':')
        game_id = game_label[5:]
        game_record[game_id] = []

        for sample in game.split(';'):
            sample_dict = {
                'red'  : 0,
                'green': 0,
                'blue' : 0
            }
            color_count_regex = r'(?:(?P<red>\d+) red)|(?:(?P<green>\d+) green)|(?:(?P<blue>\d+) blue)'

            # Using re.search only returns the first match, while re.findall returns a list (so doesn't use group labels)
            # Using re.finditer gets all matches as match objects (including group names), but each match is a separate item
            # It seems like there should be a way to get a single match object with multiple labeled groups, but I'm not sure how
            for color_match in re.finditer(color_count_regex, sample):
                sample_dict.update({ color: int(count) for color, count in color_match.groupdict().items() if count })

            game_record[game_id].append(sample_dict)

    return game_record