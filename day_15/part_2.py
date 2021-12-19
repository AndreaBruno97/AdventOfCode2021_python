import common.file_read as fr
import sys

matrix = fr.open_file_int_matrix()
rows = len(matrix)
cols = len(matrix[0])
reps = 5
max_cell_val = 9
size_r = rows * reps
size_c = cols * reps

dp_storage = []
for i in range(size_r):
    dp_storage.append([None] * size_c)

for line in range(size_r + size_c, -1, -1):
    base_r = min(line, size_r-1)
    cur_num = line + 1
    if cur_num > size_r:
        cur_num = 2*size_r - line - 1
    base_c = max(0, line-size_r+1)

    for i in range(base_r-base_c+1):
        cur_r = base_r-i
        cur_c = base_c+i

        if cur_r == size_r - 1 and cur_c == size_c - 1:
            min_down = 0
            min_right = 0
        else:
            if cur_r + 1 < size_r:
                min_down = dp_storage[cur_r+1][cur_c]
            else:
                min_down = sys.maxsize

            if cur_c + 1 < size_c:
                min_right = dp_storage[cur_r][cur_c+1]
            else:
                min_right = sys.maxsize

        cur_value = (matrix[cur_r % rows][cur_c % cols] + int(cur_r/rows) + int(cur_c/cols))
        if cur_value > max_cell_val:
            cur_value = cur_value % max_cell_val

        dp_storage[cur_r][cur_c] = min(min_down, min_right) + cur_value

print(dp_storage[0][0] - matrix[0][0])

val = 8
for r in range(5):
    for c in range(5):
        cur_v = val + r + c
        if cur_v > max_cell_val:
            cur_v = cur_v%max_cell_val
        print(cur_v,end=" ")
    print("")
print(dp_storage[-1][-1], dp_storage[-1][-2], dp_storage[-2][-1])
