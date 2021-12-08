import common.file_read as fr

file = fr.open_file_lines()

target_digit_size = [2, 4, 3, 7]
counter = 0
for line in file:
    for num in [len(x) for x in line.split(" | ")[1].strip().split(" ")]:
        if num in target_digit_size:
            counter += 1

print(counter)