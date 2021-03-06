import numpy as np


def part1(bingo_data):
    print('Q: What will your final score be if you choose that board?')
    final_score = 0

    (bingo_numbers, np_bingo_boards, np_bingo_boards_marked) = get_bingo_numbers_and_np_boards(bingo_data)

    # Start calling bingo numbers
    for i, number in enumerate(bingo_numbers):
        np_bingo_boards_marked = call_number(number, np_bingo_boards, np_bingo_boards_marked)

        bingo_board_indices = check_boards_for_bingo(np_bingo_boards_marked)

        if bingo_board_indices:
            first_bingo_idx = bingo_board_indices[0]
            final_score = get_bingo_board_score(np_bingo_boards[first_bingo_idx], np_bingo_boards_marked[first_bingo_idx], number)
            break

    print(f'A: {final_score}')


def get_bingo_numbers_and_np_boards(bingo_data):
    bingo_numbers = bingo_data.readline().split(',')
    bingo_boards = ''.join(bingo_data.readlines()[1:]).split('\n\n')

    # Create numpy arrays of each board and add to list 'np_bingo_boards'
    np_bingo_boards = []
    np_bingo_boards_marked = []
    for board in bingo_boards:
        # Split board into list of rows
        board_rows = board.split('\n')

        # Split rows of boards into columns (list of lists)
        board_lol = [x.split() for x in board_rows]

        # Convert to numpy array and add to np_bingo_boards
        np_bingo_boards.append(np.array(board_lol))

        # Also create an empty 5x5 array to keep track of numbers called for this board
        np_bingo_boards_marked.append(np.zeros((5,5)))

    return (bingo_numbers, np_bingo_boards, np_bingo_boards_marked)


def call_number(num, np_bingo_boards, np_bingo_boards_marked):
    """Mark any boards that match the number called"""
    updated_np_bingo_boards_marked = []

    # Loop over each board
    for i, np_bingo_board in enumerate(np_bingo_boards):
        updated_marked_board = mark_board(num, np_bingo_board, np_bingo_boards_marked[i])
        updated_np_bingo_boards_marked.append(updated_marked_board)

    return updated_np_bingo_boards_marked


def mark_board(num, np_bingo_board, np_bingo_board_marked):
    """Mark board if any cells match the number called"""

    (rows, cols) = np.where(np_bingo_board == num)

    for coord in zip(rows, cols):
        np_bingo_board_marked[coord] = 1

    return np_bingo_board_marked


def check_boards_for_bingo(np_bingo_boards_marked, skip_indices=[]):
    """Check boards to see if any have gotten bingo.
    Return list of the indices of any boards that have bingo.
    """
    bingo_board_indices = []

    for board_idx, board in enumerate(np_bingo_boards_marked):
        if board_idx in skip_indices:
            continue

        bingo = board.all(axis=0).any() or board.all(axis=1).any()
        if bingo:
            bingo_board_indices.append(board_idx)

    return bingo_board_indices


def get_bingo_board_score(np_bingo_board, np_bingo_board_marked, num_last_called):
    # Get sum of all unmarked numbers on winning board
    (rows, cols) = np.where(np_bingo_board_marked == 0)

    unmarked_numbers = [ int(np_bingo_board[coord]) for coord in zip(rows, cols) ]

    score = sum(unmarked_numbers) * int(num_last_called)
    return score


def part2(bingo_data):
    print('Q: Figure out which board will win last. Once it wins, what would its final score be?')

    (bingo_numbers, np_bingo_boards, np_bingo_boards_marked) = get_bingo_numbers_and_np_boards(bingo_data)

    last_winning_score = 0
    winning_board_indices = []

    # Start calling bingo numbers
    for i, number in enumerate(bingo_numbers):
        np_bingo_boards_marked = call_number(number, np_bingo_boards, np_bingo_boards_marked)

        # bingo_board_idx = check_boards_for_bingo(np_bingo_boards_marked, winning_board_indices)
        bingo_board_indices = check_boards_for_bingo(np_bingo_boards_marked, winning_board_indices)

        for bingo_board_idx in bingo_board_indices:
            if bingo_board_idx > -1 and bingo_board_idx not in winning_board_indices:
                winning_board_indices.append(bingo_board_idx)
                last_winning_score = get_bingo_board_score(np_bingo_boards[bingo_board_idx], np_bingo_boards_marked[bingo_board_idx], number)

    print(f'A: {last_winning_score}')