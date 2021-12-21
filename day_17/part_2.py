import common.file_read as fr
import numpy as np

file = fr.open_file().replace("target area: x=", "").replace("y=", "")
target_x, target_y = [[int(y) for y in x.split("..")] for x in file.split(", ")]
sorted_target_x = [abs(target_x[0]), abs(target_x[1])]
sorted_target_y = [abs(target_y[0]), abs(target_y[1])]
sorted_target_x.sort()
sorted_target_y.sort()

x_sign = np.sign(target_x[0])
y_sign = np.sign(target_y[0])

def is_correct(cur_x, cur_y):
    pos_x = 0
    pos_y = 0
    # prev_pos_x = 1
    # prev_pos_y = 1
    max_y = -9999

    while abs(pos_x) <= sorted_target_x[1] and pos_y >= min(target_y[0], target_y[1]):
        if max_y < pos_y:
            max_y = pos_y

        if sorted_target_x[0] <= abs(pos_x) <= sorted_target_x[1] and target_y[0] <= pos_y <= target_y[1]:
            return True, max_y

        # if pos_x == prev_pos_x and pos_y == prev_pos_y :
        #     return False, max_y

        # prev_pos_x = pos_x
        # prev_pos_y = pos_y
        pos_x += cur_x
        pos_y += cur_y
        cur_x -= np.sign(cur_x)
        cur_y -= 1

    return False, max_y


range_limits_x = [x_sign, target_x[1]]
range_limits_y = [y_sign, target_y[1]]
range_limits_x.sort()
range_limits_y.sort()
range_limits_x[1] += 1
range_limits_y[1] += 1

total = 0

for x in range(*range_limits_x):
    # for y in range(*range_limits_y):
    for y in range(range_limits_y[0], 10):
        result, cur_max_y = is_correct(x, y)
        if result:
            total += 1

print(total)