import common.file_read as fr

file = fr.open_file_lines()

num_rows = len(file)
num_cols = len(file[0].strip())

height_map = [[None]*(num_cols+2)] + [[None] + [int(y) for y in x.strip()] + [None] for x in file]+ [[None]*(num_cols+2)]

counter = 0
for row in range(1, num_rows+1):
    for col in range(1, num_cols+1):
        cur = height_map[row][col]

        if all([(height_map[row+x][col+y] is None or cur < height_map[row+x][col+y]) for x,y in [[-1,0],[0,1],[1,0],[0,-1]]]):
            counter += cur + 1

print(counter)