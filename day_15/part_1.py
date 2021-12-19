import common.file_read as fr
import sys

matrix = fr.open_file_int_matrix()
rows = len(matrix)
cols = len(matrix[0])

dp_storage = []
for i in range(rows):
    dp_storage.append([None] * cols)

dp_storage[rows-1][cols-1] = matrix[rows-1][cols-1]


def find_path(cur_r, cur_c):
    min_down = sys.maxsize
    min_right = sys.maxsize

    if cur_r + 1 < rows:
        if dp_storage[cur_r+1][cur_c] is None:
            find_path(cur_r + 1, cur_c)
        min_down = dp_storage[cur_r+1][cur_c]

    if cur_c + 1 < cols:
        if dp_storage[cur_r][cur_c+1] is None:
            find_path(cur_r, cur_c + 1)
        min_right = dp_storage[cur_r][cur_c+1]

    dp_storage[cur_r][cur_c] = min(min_down, min_right) + matrix[cur_r][cur_c]


find_path(0, 0)
print(dp_storage[0][0] - matrix[0][0])
