import re


def parse_input(input_file):
    crates = { x: [] for x in range(1, 10) }
    rearrangement_procedure = []
    procedure_regex = re.compile('move (\d+) from (\d) to (\d)')

    for line in input_file.readlines():
        if line.startswith(' 1'):
            continue

        line = line.rstrip()
        procedure_match = procedure_regex.match(line)
        if procedure_match:
            procedure_instruction = ( int(procedure_match.group(1)), int(procedure_match.group(2)), int(procedure_match.group(3)) )
            rearrangement_procedure.append(procedure_instruction)
        else:
            char_positions = [ x for x in range(1, len(line), 4) ]
            for column_idx in range(len(char_positions)):
                char_position = char_positions[column_idx]
                if line[char_position] != ' ':
                    crates[column_idx+1].insert(0, line[char_position])

    return { 'crates': crates, 'rearrangement_procedure': rearrangement_procedure }


def part1(puzzle_input):
    print('Q: After the rearrangement procedure completes, what crate ends up on top of each stack?')

    crates = puzzle_input['crates']
    rearrangement_procedure = puzzle_input['rearrangement_procedure']

    for procedure in rearrangement_procedure:
        for n in range(procedure[0]):
            crates = move_crate(crates, procedure[1], procedure[2])

    ans = ''
    for i in range(1, 10):
        if len(crates[i]):
            ans += crates[i].pop()

    print(f'A: {ans}')


def move_crate(crates, from_stack, to_stack):
    try:
        crate_moving = crates[from_stack].pop()
        crates[to_stack].append(crate_moving)
    except:
        pass

    return crates


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')