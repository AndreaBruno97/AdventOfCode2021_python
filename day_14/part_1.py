import common.file_read as fr
from collections import Counter

file = fr.open_file_lines()

steps = 10

template = file[0].strip()
pairs = {}
for line in file[2:]:
    target, new_ch = line.strip().split(" -> ")
    pairs[target] = new_ch

for step in range(steps):
    new_template = ""

    for i in range(1,len(template)):
        cur_match = template[i-1:i+1]

        new_template += template[i-1]
        if cur_match in pairs:
            new_template += pairs[cur_match]

    new_template += template[-1]
    template = new_template

result = list(Counter(template).values())
result.sort()
print(result[-1] - result[0])
