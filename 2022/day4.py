# example_puzzle_input = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
def part1(puzzle_input):
    print('Q: In how many assignment pairs does one range fully contain the other?')

    complete_overlap_count = 0
    for i in range(0, len(puzzle_input)):
        (pair_1, pair_2) = puzzle_input[i].split(',')
        pair_1 = pair_1.split('-')
        pair_2 = pair_2.split('-')

        sections_1 = { x for x in range(int(pair_1[0]), int(pair_1[1]) +1) }
        sections_2 = { x for x in range(int(pair_2[0]), int(pair_2[1]) +1) }

        if sections_1.issubset(sections_2) or sections_1.issuperset(sections_2):
            complete_overlap_count += 1

    ans = complete_overlap_count

    print(f'A: {ans}')


def part2(puzzle_input):
    print('Q: In how many assignment pairs do the ranges overlap?')

    partial_overlap_count = 0
    for i in range(0, len(puzzle_input)):
        (pair_1, pair_2) = puzzle_input[i].split(',')
        pair_1 = pair_1.split('-')
        pair_2 = pair_2.split('-')

        sections_1 = { x for x in range(int(pair_1[0]), int(pair_1[1]) +1) }
        sections_2 = { x for x in range(int(pair_2[0]), int(pair_2[1]) +1) }

        if bool(sections_1.intersection(sections_2)):
            partial_overlap_count += 1

    ans = partial_overlap_count

    print(f'A: {ans}')