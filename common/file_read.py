def open_file(filename):
    with open(filename) as f:
        content = f.read()
    return content


def open_file_lines(filename):
    with open(filename) as f:
        content = f.readlines()
    return content
