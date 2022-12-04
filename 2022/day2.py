opponent_shape_codes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

shape_scores = {
    'rock'    : 1,
    'paper'   : 2,
    'scissors': 3,
}

outcome_scores = {
    'win' : 6,
    'lose': 0,
    'draw': 3
}

def part1(puzzle_input):
    print('Q: What would your total score be if everything goes exactly according to your strategy guide?')

    my_shape_codes = {
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
    }

    my_total_score = 0
    for codes in puzzle_input:
        (opponent_shape_code, my_shape_code) = codes.split()
        opponent_shape = opponent_shape_codes[opponent_shape_code]

        my_shape = my_shape_codes[my_shape_code]
        my_total_score += shape_scores[my_shape]

        winner = play(opponent_shape, my_shape)
        if winner == 0:
            my_total_score += outcome_scores['draw']
        elif winner == 2:
            my_total_score += outcome_scores['win']

    ans = my_total_score

    print(f'A: {ans}')


def play(shape1, shape2):
    """Given the shapes thrown by players 1 and 2, returns 0 if it is a draw, otherwise, the number of the winning player"""
    winner = 0

    if shape1 == 'rock':
        if shape2 == 'paper':
            winner = 2
        elif shape2 == 'scissors':
            winner = 1
    elif shape1 == 'paper':
        if shape2 == 'rock':
            winner = 1
        elif shape2 == 'scissors':
            winner = 2
    elif shape1 == 'scissors':
        if shape2 == 'rock':
            winner = 2
        elif shape2 == 'paper':
            winner = 1

    return winner


def part2(puzzle_input):
    print("Q: Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?")

    shape_for_outcome_against_shape = {
        'win': {
            'rock'    : 'paper',
            'paper'   : 'scissors',
            'scissors': 'rock'
        },
        'lose': {
            'rock'    : 'scissors',
            'paper'   : 'rock',
            'scissors': 'paper'
        },
        'draw': {
            'rock'    : 'rock',
            'paper'   : 'paper',
            'scissors': 'scissors'
        }
    }

    desired_outcome_from_code = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
    }

    my_total_score = 0
    for codes in puzzle_input:
        (opponent_shape_code, my_instruction) = codes.split()
        opponent_shape = opponent_shape_codes[opponent_shape_code]

        desired_outcome = desired_outcome_from_code[my_instruction]
        my_shape = shape_for_outcome_against_shape[desired_outcome][opponent_shape]
        my_total_score += shape_scores[my_shape]

        winner = play(opponent_shape, my_shape)
        if winner == 0:
            my_total_score += outcome_scores['draw']
        elif winner == 2:
            my_total_score += outcome_scores['win']

    ans = my_total_score

    print(f'A: {ans}')