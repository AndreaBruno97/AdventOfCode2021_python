import common.file_read as fr

def get_dict_reversed(diction, target):
    return {key for key,value in diction.items() if value==target}


file = fr.open_file_lines()

standard_display = [                        # Num       Digits
    {'a', 'b', 'c', 'e', 'f', 'g'},         # 0         6
    {'c', 'f'},                             # 1         2
    {'a', 'c', 'd', 'e', 'g'},              # 2         5
    {'a', 'c', 'd', 'f', 'g'},              # 3         5
    {'b', 'c', 'd', 'f'},                   # 4         4
    {'a', 'b', 'd', 'f', 'g'},              # 5         5
    {'a', 'b', 'd', 'e', 'f', 'g'},         # 6         6
    {'a', 'c', 'f'},                        # 7         3
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},    # 8         7
    {'a', 'b', 'c', 'd', 'f', 'g'},         # 9         6
]
unique_digit_nums = [1, 4, 7, 8]
segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

total = 0

for line in file:
    patterns, numbers = line.strip().split(" | ")
    patterns = [{y for y in x} for x in patterns.split()]
    numbers = [{y for y in x} for x in numbers.split()]
    # print(patterns, numbers)

    # key: segment in the string, value: actual segment
    segments_dict = {x: '' for x in segments}

    # Deciphering segments

    segments_frequency = [0] * len(segments)
    for pattern in patterns:
        for segm in pattern:
            segments_frequency[segments.index(segm)] += 1
    # 'e' is the only segment present 4 times
    segments_dict[segments[segments_frequency.index(4)]] = 'e'
    # 'b' is the only segment present 6 times
    segments_dict[segments[segments_frequency.index(6)]] = 'b'
    # 'f' is the only segment present 9 times
    segments_dict[segments[segments_frequency.index(9)]] = 'f'

    one = [x for x in patterns if len(x)==2][0]
    seven = [x for x in patterns if len(x)==3][0]
    four = [x for x in patterns if len(x)==4][0]
    eight = [x for x in patterns if len(x)==7][0]

    segments_dict[list(seven - one)[0]] = 'a'
    segments_dict[list(eight - four - seven - get_dict_reversed(segments_dict, 'e'))[0]] = 'g'
    segments_dict[list(one - get_dict_reversed(segments_dict, 'f'))[0]] = 'c'
    segments_dict[list(four
                       - get_dict_reversed(segments_dict, 'b')
                       - get_dict_reversed(segments_dict, 'c')
                       - get_dict_reversed(segments_dict, 'f')
                       )[0]] = 'd'

    # Deciphering numbers
    actual_num = 0

    for number in numbers:
        actual_segment = {segments_dict[x] for x in number}
        actual_num = (10 * actual_num) + standard_display.index(actual_segment)

    total += actual_num

print(total)