def part1(lanternfish_timers_str):
    print('Q: How many lanternfish would there be after 80 days?')
    lanternfish_timers_final = [int(x) for x in ''.join(lanternfish_timers_str.readlines()).split(',')]

    for day in range(80):
        lanternfish_timers_final = one_day_passes(lanternfish_timers_final)

    ans = len(lanternfish_timers_final)

    print(f'A: {ans}')


def one_day_passes(lanternfish_timers):
    lanternfish_timers_tomorrow = []
    num_new_lanternfish = 0

    for fish_timer in lanternfish_timers:
        if fish_timer == 0:
            num_new_lanternfish += 1
            lanternfish_timers_tomorrow.append(6)
        else:
            lanternfish_timers_tomorrow.append(fish_timer-1)

    lanternfish_timers_tomorrow += [8 for x in range(num_new_lanternfish)]

    return lanternfish_timers_tomorrow


def part2(lanternfish_timers_str):
    print('Q: How many lanternfish would there be after 256 days?')
    lanternfish_timers_list = [int(x) for x in ''.join(lanternfish_timers_str.readlines()).split(',')]

    # Get dictionary containing initial number of fish with each possible timer value
    lanternfish_timers_dict = get_empty_timers_dict()
    for timer_value in lanternfish_timers_dict:
        lanternfish_timers_dict[timer_value] += lanternfish_timers_list.count(timer_value)

    # Update dictionary with final number of fish with each final possible timer value after 256 days
    for day in range(256):
        lanternfish_timers_dict = one_day_passes_more_efficiently(lanternfish_timers_dict)

    # Count all the fish to get the answer
    ans = sum(lanternfish_timers_dict.values())

    print(f'A: {ans}')


def get_empty_timers_dict():
    empty_timers_dict = {}
    possible_timer_values = range(9)

    for x in possible_timer_values:
        empty_timers_dict[x] = 0

    return empty_timers_dict


def one_day_passes_more_efficiently(lanternfish_timers_dict):
    # Copy current lanternfish_timers_dict over to new dict
    new_lanternfish_timers_dict = {}
    for timer_val in lanternfish_timers_dict:
        new_lanternfish_timers_dict[timer_val] = lanternfish_timers_dict[timer_val]

    # Age each lanternfish, spawning new fish as appropriate
    for timer_val in lanternfish_timers_dict:
        num_with_current_val = lanternfish_timers_dict[timer_val]

        if timer_val == 0:
            new_lanternfish_timers_dict[8] += num_with_current_val
            new_lanternfish_timers_dict[6] += num_with_current_val
        else:
            new_lanternfish_timers_dict[timer_val-1] += num_with_current_val

        new_lanternfish_timers_dict[timer_val] -= num_with_current_val

    return new_lanternfish_timers_dict