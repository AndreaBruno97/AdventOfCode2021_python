import common.file_read as fr

commands = fr.open_file_lines()
cur_x = 0
cur_y = 0

for command in commands:
    [direction, units] = command.split()
    units = int(units)

    if direction == "forward":
        cur_x += units
    if direction == "down":
        cur_y += units
    if direction == "up":
        cur_y -= units

print(cur_x * cur_y)