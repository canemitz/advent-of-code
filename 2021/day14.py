def part1(input_data):
    print('Q: What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?')
    (polymer_template, pair_insertion_rules) = parse_input(input_data)

    polymer = apply_pair_insertion(polymer_template, pair_insertion_rules, 10)

    element_quantities = get_element_quantities(polymer)
    most_common  = max(element_quantities, key=element_quantities.get)
    least_common = min(element_quantities, key=element_quantities.get)

    ans = element_quantities[most_common] - element_quantities[least_common]

    print(f'A: {ans}')


def parse_input(input_data):
    polymer_template = input_data.readline().strip()

    pair_insertion_rules = {}
    for rule in input_data.readlines():
        rule = rule.strip()
        if rule:
            [pair, element] = rule.split(' -> ')
            pair_insertion_rules[pair] = element

    return (polymer_template, pair_insertion_rules)


def apply_pair_insertion(polymer_template, pair_insertion_rules, n_steps):
    polymer = polymer_template

    for i in range(n_steps):
        pairs = [ polymer[x:x+2] for x in range(len(polymer)-1) ]

        new_polymer = polymer[0]
        for pair in pairs:
            if pair in pair_insertion_rules:
                new_polymer += pair_insertion_rules[pair]
            new_polymer += pair[1]

        polymer = new_polymer

    return polymer


def get_element_quantities(polymer):
    polymer_set = set([element for element in polymer])

    element_quantities = {}
    for element in polymer_set:
        element_quantities[element] = polymer.count(element)

    return element_quantities


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')