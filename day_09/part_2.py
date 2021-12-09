import common.file_read as fr


def basin_size(height_map, visited, cur_row, cur_col, total):
    visited[cur_row][cur_col] = True

    for x,y in [[-1,0],[0,1],[1,0],[0,-1]]:
        new_row = cur_row+x
        new_col = cur_col+y

        if visited[new_row][new_col]:
            continue

        total = basin_size(height_map, visited, new_row, new_col, total)

    return total + 1


file = fr.open_file_lines()

basin_limit = 9

num_rows = len(file)
num_cols = len(file[0].strip())

height_map = [[None]*(num_cols+2)] + [[None] + [int(y) for y in x.strip()] + [None] for x in file]+ [[None]*(num_cols+2)]

low_points = set()
for row in range(1, num_rows+1):
    for col in range(1, num_cols+1):
        cur = height_map[row][col]

        if all([(height_map[row+x][col+y] is None or cur < height_map[row+x][col+y]) for x,y in [[-1,0],[0,1],[1,0],[0,-1]]]):
            low_points.add((row, col))


visited = [[y is None or y==basin_limit for y in x] for x in height_map]
basin_sizes = [basin_size(height_map, visited, x, y, 0) for x,y in low_points]

basin_sizes.sort()
basin_sizes = basin_sizes[-3:]

print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
