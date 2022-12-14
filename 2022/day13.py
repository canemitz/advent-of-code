import ast


def part1(puzzle_input):
    print('Q: Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?')

    # True if packet pair at that index is in order
    packet_pair_in_order = [ compare_pair(*packet_pair) for packet_pair in puzzle_input ]

    # Packet pairs have one-based indexing
    indices_of_packet_pairs_in_order = [ i+1 for i in range(len(packet_pair_in_order)) if packet_pair_in_order[i] ]

    ans = sum(indices_of_packet_pairs_in_order)
    print(f'A: {ans}')


def part1_verbose(puzzle_input):
    print('Q: Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?')

    # True if packet pair at that index is in order
    packet_pairs_in_order = []
    for i in range(len(puzzle_input)):
        packet_pair = puzzle_input[i]
        pair_num = i+1
        print(f'\n== Pair {pair_num} ==')
        packet_pairs_in_order.append(compare_pair_verbose(*packet_pair))

    # Packet pairs have one-based indexing
    indices_of_packet_pairs_in_order = [ i+1 for i in range(len(packet_pairs_in_order)) if packet_pairs_in_order[i] ]

    print(f'\npacket_pairs_in_order: {packet_pairs_in_order}')
    print(f'indices_of_packet_pairs_in_order: {indices_of_packet_pairs_in_order}\n')

    ans = sum(indices_of_packet_pairs_in_order)
    print(f'A: {ans}')


def compare_pair(left, right):
    """Compare two values. Return True if the pairs are in order, False if not, and None if indeterminate."""
    items_in_correct_order = None

    if type(left) == int and type(right) == int:
        # If left and right are equal, ordering is indeterminate
        # Otherwise, items are in order if the left is less than the right
        if left != right:
            items_in_correct_order = left < right
    elif type(left) == list and type(right) == list:
        # If left list runs out of items first, items are in order
        # If right list runs out of items first, items are not in order
        # If elements i in left and right lists indicate correct or incorrect ordering, use that
        max_len = max(len(left), len(right))
        for i in range(max_len):
            if i+1 > len(left):
                items_in_correct_order = True
                break

            elif i+1 > len(right):
                items_in_correct_order = False
                break

            sub_compare = compare_pair(left[i], right[i])
            if type(sub_compare) is bool:
                items_in_correct_order = sub_compare
                break
    else:
        # Convert whichever value is not a list to a list, then retry the comparison
        if type(left) == list:
            right = [right]
        else:
            left = [left]
        items_in_correct_order = compare_pair(left, right)

    return items_in_correct_order


def compare_pair_verbose(left, right, indent=''):
    """Compare two values. Return True if the pairs are in order, False if not, and None if indeterminate."""
    items_in_correct_order = None

    print(f'{indent}- Compare {left} vs {right}')
    indent += '  '

    if type(left) == int and type(right) == int:
        # If left and right are equal, ordering is indeterminate
        # Otherwise, items are in order if the left is less than the right
        if left != right:
            if left < right:
                print(f'{indent}- Left side is smaller, so inputs are in the right order')
            else:
                print(f'{indent}- Right side is smaller, so inputs are not in the right order')
            items_in_correct_order = left < right
    elif type(left) == list and type(right) == list:
        # If left list runs out of items first, items are in order
        # If right list runs out of items first, items are not in order
        # If elements i in left and right lists indicate correct or incorrect ordering, use that
        max_len = max(len(left), len(right))
        for i in range(max_len):
            if i+1 > len(left):
                print(f'{indent}- Left side ran out of items, so inputs are in the right order')
                items_in_correct_order = True
                break

            elif i+1 > len(right):
                print(f'{indent}- Right side ran out of items, so inputs are not in the right order')
                items_in_correct_order = False
                break

            sub_compare = compare_pair_verbose(left[i], right[i], indent)
            if type(sub_compare) is bool:
                items_in_correct_order = sub_compare
                break
    else:
        # Convert whichever value is not a list to a list, then retry the comparison
        if type(left) == list:
            print(f'{indent}- Mixed types; convert right to [{right}] and retry comparison')
            right = [right]
        else:
            print(f'{indent}- Mixed types; convert left to [{left}] and retry comparison')
            left = [left]
        items_in_correct_order = compare_pair_verbose(left, right, indent)

    return items_in_correct_order


def part2(puzzle_input):
    print('Q: Organize all of the packets into the correct order. What is the decoder key for the distress signal?')
    packets = []
    for packet_pair in puzzle_input:
        packets += list(packet_pair)

    divider_packets = [ [[2]], [[6]] ]
    packets += divider_packets

    sorted_packets = bubble_sort(packets)

    # Packets have one-based indexing
    divider_packet_idx_0 = sorted_packets.index(divider_packets[0]) + 1
    divider_packet_idx_1 = sorted_packets.index(divider_packets[1]) + 1

    decoder_key = f'{divider_packet_idx_0} * {divider_packet_idx_1}'
    ans = f'{decoder_key} = {eval(decoder_key)}'

    print(f'A: {ans}')


def part2_verbose(puzzle_input):
    print('Q: Organize all of the packets into the correct order. What is the decoder key for the distress signal?')
    packets = []
    for packet_pair in puzzle_input:
        packets += list(packet_pair)

    divider_packets = [ [[2]], [[6]] ]
    packets += divider_packets

    sorted_packets = bubble_sort(packets)

    print('\nPackets in the correct order:\n')
    for packet in sorted_packets:
        print(packet)
    print()

    # Packets have one-based indexing
    divider_packet_idx_0 = sorted_packets.index(divider_packets[0]) + 1
    divider_packet_idx_1 = sorted_packets.index(divider_packets[1]) + 1

    decoder_key = f'{divider_packet_idx_0} * {divider_packet_idx_1}'
    ans = f'{decoder_key} = {eval(decoder_key)}'

    print(f'A: {ans}')


def bubble_sort(_list):
    n = len(_list)

    for _ in range(n):
        is_sorted = True

        for i in range(n - 1):
            left  = _list[i]
            right = _list[i+1]

            if not compare_pair(left, right):
                _list[i], _list[i+1] = right, left
                is_sorted = False

        if is_sorted:
            break

    return _list


def parse_input(input_file_obj):
    packet_pair_strs = input_file_obj.read().strip().split('\n\n')

    packet_pairs = [
        tuple( ast.literal_eval(packet) for packet in packet_pair.split('\n') )
        for packet_pair in packet_pair_strs
    ]

    return packet_pairs