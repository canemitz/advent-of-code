def part1(puzzle_input):
    global num_mixes

    if not running_part2():
        print('Q: Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?')
        num_mixes = 1

    mixed_file = get_mixed_file(puzzle_input, num_mixes)
    grove_coords = find_grove_coords(mixed_file)
    ans = sum(grove_coords)

    print(f'A: {ans}')


def part1_verbose(puzzle_input):
    global num_mixes

    if not running_part2():
        print('Q: Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?')
        num_mixes = 1

    print(f'Initial arrangement:')
    input(', '.join(puzzle_input))

    mixed_file = get_mixed_file_verbose(puzzle_input, num_mixes)
    grove_coords = find_grove_coords(mixed_file)

    print()
    for i in range(len(grove_coords)):
        print(f'The {i+1}000th number after 0 is {grove_coords[i]}.')

    ans = f'{grove_coords[0]} + {grove_coords[1]} + {grove_coords[2]} = {sum(grove_coords)}'

    print(f'A: {ans}')


def get_mixed_file(file, num_mixes):
    # Store numbers in file as list of dictionaries keyed by initial index
    file_dicts = [ { i: int(file[i]) } for i in range(len(file)) ]

    for i in range(num_mixes):
        for j in range(len(file_dicts)):
            file_dicts = mix_file(file_dicts, j)

    mixed_file = [ get_element_value(x) for x in file_dicts ]
    return mixed_file


def get_mixed_file_verbose(file, num_mixes):
    # Store numbers in file as list of dictionaries keyed by initial index
    file_dicts = [ { i: int(file[i]) } for i in range(len(file)) ]

    for i in range(num_mixes):
        for j in range(len(file_dicts)):
            file_dicts = mix_file_verbose(file_dicts, j)

        mixed_file = [ get_element_value(x) for x in file_dicts ]

        if running_part2():
            round_noun = 'rounds' if i else 'round'
            print(f'\nAfter {i+1} {round_noun} of mixing:')
            input(', '.join([ str(x) for x in mixed_file ]))

    return mixed_file


def mix_file(file_dicts, original_idx):
    current_idx = get_current_idx(file_dicts, original_idx)
    instruction = file_dicts[current_idx][original_idx]

    file_dicts = move_element(file_dicts, current_idx, instruction)
    return file_dicts


def mix_file_verbose(file_dicts, original_idx):
    current_idx = get_current_idx(file_dicts, original_idx)
    instruction = file_dicts[current_idx][original_idx]

    if running_part2():
        file_dicts = move_element(file_dicts, current_idx, instruction)
    else:
        file_dicts = move_element_verbose(file_dicts, current_idx, instruction)

    return file_dicts


def get_element_value(element_dict):
    return list(element_dict.values())[0]


def get_current_idx(file_dicts, original_idx):
    # Get list where the current_idx'th element is true (since all number dict keys are unique)
    file_bool_list = list(map( lambda n_dict: original_idx in n_dict, file_dicts ) )
    current_idx = file_bool_list.index(True)
    return current_idx


def move_element(file_dicts, current_idx, instruction):
    element = file_dicts.pop(current_idx)

    max_idx = len(file_dicts)
    insert_idx = (current_idx + instruction) % max_idx
    if insert_idx == 0:
        insert_idx = max_idx

    file_dicts.insert(insert_idx, element)

    return file_dicts


def move_element_verbose(file_dicts, current_idx, instruction):
    element = file_dicts.pop(current_idx)

    max_idx = len(file_dicts)
    insert_idx = (current_idx + instruction) % max_idx
    if insert_idx == 0:
        insert_idx = max_idx

    file_dicts.insert(insert_idx, element)

    current_arrangement = [ str( get_element_value(x) ) for x in file_dicts ]
    element_value = str( get_element_value(element) )
    if current_idx != insert_idx:
        left_value = get_element_value(file_dicts[insert_idx-1])
        right_idx = insert_idx + 1 if insert_idx < max_idx  else 0
        right_value = str( get_element_value(file_dicts[right_idx]) )
        print(f'\n{element_value} moves between {left_value} and {right_value}:')
    else:
        print(f'\n{element_value} does not move:')
    input(', '.join(current_arrangement))

    return file_dicts


def find_grove_coords(file):
    grove_coords = []

    idx_of_zero = file.index(0)
    for idx in [1000, 2000, 3000]:
        coord_idx = (idx_of_zero + idx) % len(file)
        grove_coords.append(file[coord_idx])

    return grove_coords


def part2(puzzle_input):
    print('Q: Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?')

    # Store numbers in file as list of dictionaries keyed by initial index
    decryption_key = 811589153
    decrypted_puzzle_input = [str(decryption_key*int(x)) for x in puzzle_input]
    decrypted_file = [ { i: int(decrypted_puzzle_input[i]) } for i in range(len(decrypted_puzzle_input)) ]

    global part
    global num_mixes

    part = 2
    num_mixes = 10

    part1(decrypted_puzzle_input)


def part2_verbose(puzzle_input):
    """Interestingly, this shows that the arrangement of the example is different than shown.
       My code matches Eric's example output, except his always has 0 at the beginning, while the zero
       in mine never is at the start, but moves around various places towards the end of the arrangement.
       Nevertheless, I get the correct final answer. Also, part1_verbose shows the same arrangement as the example.
    """
    print('Q: Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?')

    # Store numbers in file as list of dictionaries keyed by initial index
    decryption_key = 811589153
    decrypted_puzzle_input = [str(decryption_key*int(x)) for x in puzzle_input]
    decrypted_file = [ { i: int(decrypted_puzzle_input[i]) } for i in range(len(decrypted_puzzle_input)) ]

    global part
    global num_mixes

    part = 2
    num_mixes = 10

    part1_verbose(decrypted_puzzle_input)


def running_part2():
    """We define the global part in part2, but not part1, so we can test whether that variable is defined to determine which part we're running."""
    global part

    try:
        return part == 2
    except:
        return False