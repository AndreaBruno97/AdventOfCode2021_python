import common.file_read as fr

numbers = [x.strip() for x in fr.open_file_lines()]

size = len(numbers[0].strip())
oxygen_numbers = numbers.copy()
co2_numbers = numbers.copy()

oxygen_rating = 0
co2_rating = 0

for cur_computation in ["oxygen", "co2"]:
    if cur_computation == "oxygen":
        gas_numbers = oxygen_numbers
    else:
        gas_numbers = co2_numbers

    for i in range(size):
        if len(gas_numbers) == 1:
            break

        counter_ones = 0
        cur_size = len(gas_numbers)

        for num in gas_numbers:
            if num[i] == "1":
                counter_ones += 1

        comparison = "1"
        if (cur_computation=="oxygen" and counter_ones < cur_size / 2) or (cur_computation=="co2" and counter_ones >= cur_size / 2):
            comparison = "0"

        new_gas_numbers = []
        for num in gas_numbers:
            if num[i] == comparison:
                new_gas_numbers.append(num)
        gas_numbers = new_gas_numbers

    if cur_computation == "oxygen":
        oxygen_rating = int(gas_numbers[0], base=2)
    else:
        co2_rating = int(gas_numbers[0], base=2)

print(oxygen_rating * co2_rating)
