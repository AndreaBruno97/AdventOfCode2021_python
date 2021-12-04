import common.file_read as fr
import numpy as np

file = fr.open_file()

file = file.split("\n\n")
numbers = file[0].split(",")
boards = [x.split("\n") for x in file[1:]]
boards = [[row.split() for row in board] for board in boards]
boards = [np.array(board) for board in boards]

board_size = boards[0].shape
board_len = board_size[0]
boards_matches = [np.zeros(board_size, dtype=int) for x in boards]

last_number = None
winning_sum = None

for number in numbers:
    if last_number is not None:
        break

    for i in range(len(boards)):
        if number in boards[i]:
            position = np.where(boards[i] == number)
            boards_matches[i][position] = 1
            row = position[0][0]
            col = position[1][0]

            if np.sum(boards_matches[i][row]) == board_len or np.sum(boards_matches[i][:, col]) == board_len:
                winning_sum = np.sum(boards[i].astype(np.int), where=np.logical_not(boards_matches[i]))

            if winning_sum is not None:
                last_number = int(number)
                break

print(last_number * winning_sum)