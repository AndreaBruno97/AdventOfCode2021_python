import common.file_read as fr

file = fr.open_file()

positions = [int(x) for x in file.split(",")]

fuel = None
for align in range(min(positions), max(positions)):
    cur_fuel = 0
    for x in positions:
        delta = abs(align - x)
        cur_fuel += ( (1 + delta) * int(delta/2) )+ ( (int(delta/2) + 1) * (delta%2) )

    if fuel is None or cur_fuel < fuel:
        fuel = cur_fuel

print(fuel)
