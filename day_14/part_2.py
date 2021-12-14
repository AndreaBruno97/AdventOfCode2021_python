import common.file_read as fr
from collections import Counter

file = fr.open_file_lines()

steps = 41

template = file[0].strip()
pairs = {}
for line in file[2:]:
    target, new_ch = line.strip().split(" -> ")
    pairs[target] = new_ch

char_set = set("".join(pairs.keys()))
char_counter = {ch: 0 for ch in char_set}
dp_memory = {}
for pair in pairs.keys():
    dp_memory[pair] = [None] * steps


def sum_counters(counter1, counter2):
    result = char_counter.copy()
    for ch in char_set:
        result[ch] = counter1[ch] + counter2[ch]
    return result


def recursive_counter(left, right, pos):
    if pos == steps-1:
        new_char_counter = char_counter.copy()
        if dp_memory[left+right][pos] is None:
            new_char_counter[left] += 1
            new_char_counter[right] += 1
            dp_memory[left+right][pos] = new_char_counter

        return dp_memory[left+right][pos]

    middle = pairs[left+right]

    if dp_memory[left+middle][pos+1] is None:
        dp_memory[left + middle][pos + 1] = recursive_counter(left, middle, pos+1)
    if dp_memory[middle + right][pos + 1] is None:
        dp_memory[middle + right][pos + 1] = recursive_counter(middle, right, pos + 1)

    new_char_counter = dp_memory[left + middle][pos + 1].copy()
    new_char_counter = sum_counters(new_char_counter, dp_memory[middle + right][pos + 1])
    new_char_counter[middle] -= 1

    dp_memory[left + right][pos] = new_char_counter

    return new_char_counter


total_counter = char_counter.copy()
prev_ch = template[0]
for cur_ch in template[1:]:
    total_counter = sum_counters(total_counter, recursive_counter(prev_ch, cur_ch, 0))
    prev_ch = cur_ch

for ch in template[1:-1]:
    total_counter[ch] -= 1

result = list(total_counter.values())
result.sort()
print(result[-1] - result[0])
