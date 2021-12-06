import common.file_read as fr

file = fr.open_file()

max_counter = 8
max_adult_counter = 6
# Key is timer counter, value is the number of fish with that counter
timer_dict = {x: 0 for x in range(max_counter + 1)}
days = 256

for fish in [int(x) for x in file.split(",")]:
    timer_dict[fish] += 1

for i in range(days):
    new_fish_num = timer_dict[0]

    for counter in range(max_counter):
        timer_dict[counter] = timer_dict[counter+1]
    # New fish
    timer_dict[max_counter] = new_fish_num
    #Reset 0 -> 6
    timer_dict[max_adult_counter] += new_fish_num

print(sum(timer_dict.values()))