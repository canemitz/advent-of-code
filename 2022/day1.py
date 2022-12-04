def part1(puzzle_input):
    print('Q: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?')

    elf_totals = []
    current_elf_calories = 0
    for calories in puzzle_input:
        if calories == '':
            elf_totals.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(calories)

    ans = max(elf_totals)

    print(f'A: {ans}')


def part2(puzzle_input):
    print('Q: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?')

    elf_totals = []
    current_elf_calories = 0
    for calories in puzzle_input:
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