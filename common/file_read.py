def open_file(filename="input.txt"):
    with open(filename) as f:
        content = f.read()
    return content


def open_file_lines(filename="input.txt"):
    with open(filename) as f:
        content = f.readlines()
    return content


def open_file_int_array(filename="input.txt"):
    return [int(x) for x in open_file_lines(filename)]
