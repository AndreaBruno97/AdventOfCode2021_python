import common.file_read as fr


def print_dots(dots):
    max_r = max([x[0] for x in dots])
    max_c = max([x[1] for x in dots])

    for r_i in range(max_r + 1):
        for c_i in range(max_c + 1):
            if (r_i, c_i) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()


file = fr.open_file_lines()

fold_r = 'y'
fold_c = 'x'
empty_line_index = file.index("\n")

dots = set([tuple(int(x) for x in line.strip().split(",")) for line in file[:empty_line_index]])

dots = set()
for line in file[:empty_line_index]:
    c, r = line.strip().split(",")
    dots.add((int(r), int(c)))

folds = []
for line in file[empty_line_index+1:]:
    new_item = line.strip().replace("fold along ", "").split("=")
    folds.append([new_item[0], int(new_item[1])])

new_dots = set()
for dot in dots:
    direction = folds[0][0]
    size = folds[0][1]

    if direction == fold_r and dot[0] > size:
        new_dot = tuple([2*size - dot[0], dot[1]])
    elif direction == fold_c and dot[1] > size:
        new_dot = tuple([dot[0] , 2*size - dot[1]])
    else:
        new_dot = dot

    new_dots.add(new_dot)
dots = new_dots

print(len(dots))
