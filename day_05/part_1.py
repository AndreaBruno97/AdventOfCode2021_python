import common.file_read as fr

file = fr.open_file_lines()

vents = {}

for line in file:
    start, finish = line.split(" -> ")
    x1, y1 = [int(s) for s in start.split(",")]
    x2, y2 = [int(f) for f in finish.split(",")]

    new_vents = []
    if x1 == x2:
        new_vents = [(x1, new_y) for new_y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        new_vents = [(new_x, y1) for new_x in range(min(x1, x2), max(x1, x2) + 1)]

    for cur_vent in new_vents:
        if cur_vent in vents:
            vents[cur_vent] += 1
        else:
            vents[cur_vent] = 1

dangerous_vents = len([vent for vent in vents.values() if vent >= 2])

print(dangerous_vents)