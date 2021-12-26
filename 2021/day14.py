def part1(input_data):
    print('Q: What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?')
    (polymer_template, pair_insertion_rules) = parse_input(input_data)

    polymer = polymer_template
    for i in range(10):
        polymer = apply_pair_insertion(polymer, pair_insertion_rules)

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


def apply_pair_insertion(polymer, pair_insertion_rules):
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
    print('Q: What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?')
    (polymer_template, pair_insertion_rules) = parse_input(input_data)

    element_counts = {}
    for element in polymer_template:
        element_counts = add_val_to_dict_item(element_counts, element, 1)

    pair_counts = {}
    for pair in [polymer_template[x:x+2] for x in range(len(polymer_template)-1)]:
        pair_counts = add_val_to_dict_item(pair_counts, pair, 1)

    for i in range(40):
        (pair_counts, element_counts) = apply_pair_insertion_more_efficiently(pair_counts, element_counts, pair_insertion_rules)

    most_common  = max(element_counts, key=element_counts.get)
    least_common = min(element_counts, key=element_counts.get)

    ans = element_counts[most_common] - element_counts[least_common]

    print(f'A: {ans}')


def add_val_to_dict_item(dict_, key, val):
    try:
        dict_[key] += val
    except:
        dict_[key] = val

    return dict_


def apply_pair_insertion_more_efficiently(pair_counts, element_counts, pair_insertion_rules):
    new_pair_counts = pair_counts.copy()

    for pair in pair_counts:
        new_element = pair_insertion_rules[pair]
        element_counts = add_val_to_dict_item(element_counts, new_element, pair_counts[pair])

        new_pair_0 = pair[0] + new_element
        new_pair_1 = new_element + pair[1]
        num_pairs = pair_counts[pair]

        new_pair_counts = add_val_to_dict_item(new_pair_counts, new_pair_0, num_pairs)
        new_pair_counts = add_val_to_dict_item(new_pair_counts, new_pair_1, num_pairs)
        new_pair_counts = add_val_to_dict_item(new_pair_counts, pair, -num_pairs)

    return (new_pair_counts, element_counts)