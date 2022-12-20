def part1(puzzle_input):
    print('Q: Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?')

    # Store numbers in file as list of dictionaries keyed by initial index
    encrypted_file = [ { i: int(puzzle_input[i]) } for i in range(len(puzzle_input)) ]

    for i in range(len(encrypted_file)):
        encrypted_file = mix_file(encrypted_file, i)
    mixed_file = [ get_element_value(x) for x in encrypted_file ]

    grove_coords = find_grove_coords(mixed_file)
    ans = sum(grove_coords)

    print(f'A: {ans}')


def part1_verbose(puzzle_input):
    print('Q: Mix your encrypted file exactly once. What is the sum of the three numbers that form the grove coordinates?')

    # Store numbers in file as list of dictionaries keyed by initial index
    encrypted_file = [ { i: int(puzzle_input[i]) } for i in range(len(puzzle_input)) ]

    print(f'Initial arrangement:')
    input(', '.join(puzzle_input))
    for i in range(len(encrypted_file)):
        encrypted_file = mix_file_verbose(encrypted_file, i)
    mixed_file = [ get_element_value(x) for x in encrypted_file ]

    grove_coords = find_grove_coords(mixed_file)
    print()
    for i in range(len(grove_coords)):
        print(f'The {i+1}000th number after 0 is {grove_coords[i]}.')

    ans = f'{grove_coords[0]} + {grove_coords[1]} + {grove_coords[2]} = {sum(grove_coords)}'

    print(f'A: {ans}')


def mix_file(encrypted_file, original_idx):
    current_idx = get_current_idx(encrypted_file, original_idx)
    instruction = encrypted_file[current_idx][original_idx]

    encrypted_file = move_element(encrypted_file, current_idx, instruction)
    return encrypted_file


def mix_file_verbose(encrypted_file, original_idx):
    current_idx = get_current_idx(encrypted_file, original_idx)
    instruction = encrypted_file[current_idx][original_idx]

    encrypted_file = move_element_verbose(encrypted_file, current_idx, instruction)
    return encrypted_file


def get_element_value(element_dict):
    return list(element_dict.values())[0]


def get_current_idx(file, original_idx):
    # Get list where the current_idx'th element is true (since all number dict keys are unique)
    file_bool_list = list(map( lambda n_dict: original_idx in n_dict, file ) )
    current_idx = file_bool_list.index(True)
    return current_idx


def move_element(file, current_idx, instruction):
    element = file.pop(current_idx)

    max_idx = len(file)
    insert_idx = (current_idx + instruction) % max_idx
    if insert_idx == 0:
        insert_idx = max_idx

    file.insert(insert_idx, element)

    return file


def move_element_verbose(file, current_idx, instruction):
    element = file.pop(current_idx)

    max_idx = len(file)
    insert_idx = (current_idx + instruction) % max_idx
    if insert_idx == 0:
        insert_idx = max_idx

    file.insert(insert_idx, element)

    current_arrangement = [ str( get_element_value(x) ) for x in file ]
    element_value = str( get_element_value(element) )
    if current_idx != insert_idx:
        left_value = get_element_value(file[insert_idx-1])
        right_idx = insert_idx + 1 if insert_idx < max_idx  else 0
        right_value = str( get_element_value(file[right_idx]) )
        print(f'\n{element_value} moves between {left_value} and {right_value}:')
    else:
        print(f'\n{element_value} does not move:')
    input(', '.join(current_arrangement))

    return file


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
    decrypted_puzzle_input = [decryption_key*int(x) for x in puzzle_input]
    decrypted_file = [ { i: int(decrypted_puzzle_input[i]) } for i in range(len(decrypted_puzzle_input)) ]

    for j in range(10):
        for i in range(len(decrypted_file)):
            decrypted_file = mix_file(decrypted_file, i)
    mixed_file = [ get_element_value(x) for x in decrypted_file ]

    grove_coords = find_grove_coords(mixed_file)
    ans = sum(grove_coords)

    print(f'A: {ans}')


def part2_verbose(puzzle_input):
    """Interestingly, this shows that the arrangement of the example is different than shown.
       My code matches Eric's example output, except his always has 0 at the beginning, while the zero
       in mine never is at the start, but moves around various places towards the end of the arrangement.
       Nevertheless, I get the correct final answer. Also, part1_verbose shows the same arrangement as the example.
    """
    print('Q: Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?')

    # Store numbers in file as list of dictionaries keyed by initial index
    decryption_key = 811589153
    decrypted_puzzle_input = [decryption_key*int(x) for x in puzzle_input]
    decrypted_file = [ { i: int(decrypted_puzzle_input[i]) } for i in range(len(decrypted_puzzle_input)) ]

    print(f'\nInitial arrangement:')
    input(', '.join([ str(x) for x in decrypted_puzzle_input ]))

    for j in range(10):
        for i in range(len(decrypted_file)):
            decrypted_file = mix_file(decrypted_file, i)

        mixed_file = [ get_element_value(x) for x in decrypted_file ]
        round_noun = 'rounds' if j else 'round'
        print(f'\nAfter {j+1} {round_noun} of mixing:')
        input(', '.join([ str(x) for x in mixed_file ]))

    grove_coords = find_grove_coords(mixed_file)
    print()
    for i in range(len(grove_coords)):
        print(f'The {i+1}000th number after 0 is {grove_coords[i]}.')

    ans = f'{grove_coords[0]} + {grove_coords[1]} + {grove_coords[2]} = {sum(grove_coords)}'

    print(f'A: {ans}')
