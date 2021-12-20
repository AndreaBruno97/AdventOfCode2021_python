import common.file_read as fr
from functools import reduce

def to_int(cur_list):
    return int(''.join([str(x) for x in cur_list]), base=2)


def compute_packet(cur_packet):
    result = None

    cur_version = to_int(cur_packet[:3])
    cur_id = to_int(cur_packet[3:6])
    del cur_packet[:6]

    prefix = 1

    if cur_id == 4:
        cur_number = []

        while prefix == 1:
            prefix = int(cur_packet[0])
            cur_number.extend(cur_packet[1:5])
            del cur_packet[:5]

        result = to_int(cur_number)

    else:
        length_type = int(cur_packet[0])
        bit_num = 11 if length_type == 1 else 15
        operation_length = to_int(cur_packet[1:bit_num + 1])
        del cur_packet[:bit_num + 1]

        results = []

        while operation_length > 0:
            new_packet, new_result = compute_packet(cur_packet.copy())
            results.append(new_result)

            if length_type == 0:
                # packet length
                operation_length -= (len(cur_packet) - len(new_packet))
            else:
                # packet number
                operation_length -= 1

            cur_packet = new_packet

        if cur_id == 0:
            # sum
            result = sum(results)
            # print(" + ".join([str(x) for x in results]), " = ", result)
        elif cur_id == 1:
            # product
            result = reduce((lambda x, y: x * y), results)
            # print(" * ".join([str(x) for x in results]), " = ", result)
        elif cur_id == 2:
            # minimum
            result = min(results)
            # print("min(", " , ".join([str(x) for x in results]), ") = ", result)
        elif cur_id == 3:
            # maximum
            result = max(results)
            # print("max(", " , ".join([str(x) for x in results]), ") = ", result)
        elif cur_id == 5:
            # greater than
            result = int(results[0] > results[1])
            # print(results[0], " > ", results[1], " = ", result)
        elif cur_id == 6:
            # less than
            result = int(results[0] < results[1])
            # print(results[0], " < ", results[1], " = ", result)
        elif cur_id == 7:
            # equal to
            result = int(results[0] == results[1])
            # print(results[0], " == ", results[1], " = ", result)

    return cur_packet, result


file = fr.open_file()

packet_string = bin(int(file, base=16))[2:].zfill(4*len(file))
packet = [int(x) for x in packet_string]

final_packet, result = compute_packet(packet)

print(result)