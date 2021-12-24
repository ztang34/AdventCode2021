def parse_board(board_input: str):
    board = []
    rows = board_input.splitlines()
    for row_number, row in enumerate(rows):
        numbers = row.split()
        board.append([])
        for col_number, number in enumerate(numbers):
            board[row_number].append(int(number))

    return board


def calculate_col_sum(board, col_index):
    result = 0
    for row in board:
        result += row[col_index]
    return result
