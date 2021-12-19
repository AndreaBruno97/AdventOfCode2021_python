import common.file_read as fr


def to_int(cur_list):
    return int(''.join([str(x) for x in cur_list]), base=2)


file = fr.open_file()
literal_id = 4

packet_string = bin(int(file, base=16))[2:].zfill(4*len(file)).rstrip("0")
packet = [int(x) for x in packet_string]
id_stack = []
cur_number = []
operation_stack = []
version_sum = 0

while packet:
    cur_id = id_stack[-1] if id_stack else None
    cur_operation = operation_stack[-1] if operation_stack else None

    if cur_id is None:
        cur_version = to_int(packet[:3])
        id_stack.append(to_int(packet[3:6]))
        del packet[:6]
        version_sum += cur_version

    elif cur_id == literal_id:
        prefix = int(packet[0])
        cur_number.extend(packet[1:5])
        del packet[:5]

        if prefix == 0:
            # print(to_int(cur_number))
            cur_number = []
            id_stack.pop()

    else:
        length_type = int(packet[0])
        bit_num = 11 if length_type == 1 else 15
        operation_length = to_int(packet[1:bit_num+1])
        del packet[:bit_num+1]

        operation_stack.append([length_type, operation_length])

        id_stack.pop()

print(version_sum)
