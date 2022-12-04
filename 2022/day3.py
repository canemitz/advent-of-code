def part1(puzzle_input):
    print('Q: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?')

    sum_of_priorities = 0
    for rucksack_items in puzzle_input:
        split_idx = int(len(rucksack_items) / 2)
        compartment_1 = set(rucksack_items[:split_idx])
        compartment_2 = set(rucksack_items[split_idx:])

        items_in_both = compartment_1.intersection(compartment_2)
        for item in items_in_both:
            sum_of_priorities += get_priority(item)

    ans = sum_of_priorities

    print(f'A: {ans}')


def get_priority(char):
    priority = ord(char)

    if char.isupper():
        priority -= 38
    else:
        priority -= 96

    return priority

def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')