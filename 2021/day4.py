import numpy as np


def part1(bingo_data):
    print('Q: What will your final score be if you choose that board?')
    final_score = 0

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


    # Start calling bingo numbers
    for i, number in enumerate(bingo_numbers):
        np_bingo_boards_marked = call_number(number, np_bingo_boards, np_bingo_boards_marked)

        # # 5 numbers are required for bingo
        # ...but maybe a number can show up more than once, so bingo could be gotten in less than 5 number calls
        # if i < 5:
        #     continue;

        bingo_board_idx = check_boards_for_bingo(np_bingo_boards_marked)

        if bingo_board_idx > -1:
            final_score = get_bingo_board_score(np_bingo_boards[bingo_board_idx], np_bingo_boards_marked[bingo_board_idx], number)
            break

    print(f'A: {final_score}')


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


def check_boards_for_bingo(np_bingo_boards_marked):
    """Check boards to see if any have gotten bingo.
    Return the index of the first board that has bingo, or -1 if none do.
    """
    bingo_board_idx = -1

    for i, board in enumerate(np_bingo_boards_marked):
        bingo = board.all(axis=0).any() or board.all(axis=1).any()
        if bingo:
            bingo_board_idx = i
            break

    return bingo_board_idx


def get_bingo_board_score(np_bingo_board, np_bingo_board_marked, num_last_called):
    # Get sum of all unmarked numbers on winning board
    (rows, cols) = np.where(np_bingo_board_marked == 0)

    unmarked_numbers = [ int(np_bingo_board[coord]) for coord in zip(rows, cols) ]
    # for coord in zip(rows, cols):
    #     unmarked_numbers_sum += int(np_bingo_board[coord])

    score = sum(unmarked_numbers) * int(num_last_called)
    return score


def part2(bingo_data):
    print('Q: Figure out which board will win last. Once it wins, what would its final score be?')


    print(f'A: {ans}')