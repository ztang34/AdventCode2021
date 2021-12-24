from day4Helper import parse_board
from day4Helper import calculate_col_sum
from collections import OrderedDict

numbers = []
boards = []
memo = {}
with open("C:\\Users\\ztang\\Desktop\\AdventCode2021\\Day4\\Day4Input.txt") as f:
    blocks = f.read().split("\n\n")
    numbers = blocks[0].split(",")
    for index in range(1, len(blocks)):
        boards.append(parse_board(blocks[index]))
        index += 1


for number in numbers:
    memo[int(number)] = []

for board_index, board in enumerate(boards):
    for row_index, row in enumerate(board):
        for col_index, num in enumerate(row):
            if num in memo:
                memo[num].append((board_index, row_index, col_index))


winning_boards = OrderedDict()

for number in numbers:
    for board_index, row_index, col_index in memo[int(number)]:
        if board_index not in winning_boards:
            boards[board_index][row_index][col_index] = -1

        if sum(boards[board_index][row_index]) == -5 or calculate_col_sum(boards[board_index], col_index) == -5:
            if board_index not in winning_boards:
                winning_boards[board_index] = int(number)


last = winning_boards.popitem(last=True)
winning_board = boards[last[0]]
winning_num = last[1]
result = 0
for x in range(5):
    for y in range(5):
        if winning_board[x][y] != -1:
            result += winning_board[x][y]

print(result * winning_num)
