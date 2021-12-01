import common.file_read as fr

depths = fr.open_file_int_array()

counter = 0
prev_window = depths[0] + depths[1] + depths[2]
cur_window = prev_window

for i in range(3, len(depths)):
    cur_window = cur_window - depths[i-3] + depths[i]

    if cur_window > prev_window:
        counter += 1

    prev_window = cur_window

print(counter)