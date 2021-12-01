import common.file_read as fr

depths = fr.open_file_int_array()

counter = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counter += 1

print(counter)