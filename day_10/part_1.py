import common.file_read as fr

file = fr.open_file_lines()

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
values = [3, 57, 1197, 25137]

total = 0

for line in file:
    stack = []

    for ch in line:
        if ch in openings:
            stack.append(ch)
        elif ch in closings:
            position = closings.index(ch)
            if stack.pop() != openings[position]:
                total += values[position]
                break

print(total)