import common.file_read as fr

numbers = fr.open_file_lines()

total_numbers = len(numbers)
size = len(numbers[0].strip())
count_ones = [0] * size

for number in numbers:
    cur_num = [int(x) for x in number.strip()]
    for i in range(size):
        count_ones[i] += cur_num[i]

gamma_array = [0] * size
epsilon_array = [0] * size

for i in range(size):
    if count_ones[i] > total_numbers/2:
        gamma_array[i] = 1
    else:
        epsilon_array[i] = 1

gamma = int("".join([str(x) for x in gamma_array]), base=2)
epsilon = int("".join([str(x) for x in epsilon_array]), base=2)

print(gamma*epsilon)