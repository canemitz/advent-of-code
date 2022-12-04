def part1(input_data):
    print('Q: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?')

    input_arr = input_data.read().strip().split('\n')

    elf_totals = []
    current_elf_calories = 0
    for calories in input_arr:
        if calories == '':
            elf_totals.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(calories)

    ans = max(elf_totals)

    print(f'A: {ans}')


def part2(input_data):
    print('Q: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?')

    input_arr = input_data.read().strip().split('\n')

    elf_totals = []
    current_elf_calories = 0
    for calories in input_arr:
        if calories == '':
            elf_totals.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(calories)

    elf_totals.sort(reverse=True)

    top_three_totals = 0
    for i in range(3):
        top_three_totals += elf_totals[i]

    ans = top_three_totals

    print(f'A: {ans}')