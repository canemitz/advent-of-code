def part1(input_data):
    print('Q: How many measurements are larger than the previous measurement?')
    ans = 0

    prev_measurement = None
    for measurement in input_data:
        if prev_measurement and int(prev_measurement) < int(measurement):
            ans += 1
        prev_measurement = measurement

    print(f'A: {ans}')


def part2(input_data):
    print('Q: Consider sums of a three-measurement sliding window.')

    sliding_measurements = []

    window_1 = []
    window_2 = []
    window_3 = []
    for i, measurement in enumerate(input_data):

        window_1.append(int(measurement))
        if i > 0:
            window_2.append(int(measurement))
        if i > 1:
            window_3.append(int(measurement))

        if len(window_1) == 3:
            sliding_measurements.append(sum(window_1))
            window_1 = []
        if len(window_2) == 3:
            sliding_measurements.append(sum(window_2))
            window_2 = []
        if len(window_3) == 3:
            sliding_measurements.append(sum(window_3))
            window_3 = []

    part1(sliding_measurements)