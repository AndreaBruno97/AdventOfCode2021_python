import common.file_read as fr

file = fr.open_file()

positions = [int(x) for x in file.split(",")]

fuel = None
for align in range(min(positions), max(positions)):
    cur_fuel = sum([abs(align - x) for x in positions])

    if fuel is None or cur_fuel < fuel:
        fuel = cur_fuel

print(fuel)
