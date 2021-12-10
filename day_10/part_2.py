import common.file_read as fr

file = fr.open_file_lines()

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
values = [1, 2, 3, 4]
factor = 5

totals = []

for line in file:
    stack = []
    corrupted = False

    for ch in line:
        if ch in openings:
            stack.append(ch)
        elif ch in closings:
            position = closings.index(ch)
            if stack.pop() != openings[position]:
                corrupted = True
                break

    if corrupted:
        continue

    cur_points = 0

    stack.reverse()
    for elem in stack:
        cur_points *= factor
        cur_points += values[openings.index(elem)]

    totals.append(cur_points)

totals.sort()
print(totals[int(len(totals)/2)])