import common.file_read as fr
import numpy as np

matrix = np.array(fr.open_file_int_matrix())

rows = len(matrix)
cols = len(matrix[0])
total_elems = rows * cols

total = 0
steps = 0
max_level = 9
matches = set()

while len(matches) < total_elems:
    steps += 1
    matrix += 1
    flashes = 0
    matches = set()
    while np.where(matrix > max_level)[0].size > flashes:

        new_matches = set(zip(*np.where(matrix > max_level)))
        flashes = len(new_matches)

        for r, c in new_matches - matches:
            for r_i in range(max(r-1, 0), min(r+1, rows-1) + 1):
                for c_i in range(max(c-1, 0), min(c+1, cols-1) + 1):
                    if (r_i, c_i) not in matches:
                        matrix[r_i, c_i] += 1

        matches = new_matches

    for r,c in matches:
        matrix[r][c] = 0

    total += len(matches)

print(steps)