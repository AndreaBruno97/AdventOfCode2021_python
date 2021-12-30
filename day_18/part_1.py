import common.file_read as fr
import json


class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

    def get_first(self):
        first = self
        while first.left is not None:
            first = first.left
        return first

    def get_last(self):
        last = self
        while last.right is not None:
            last = last.right
        return last


def parse_num(num_array):
    if type(num_array) == int:
        # Number
        return Node(int(num_array))

    left_node = parse_num(num_array[0])
    right_node = parse_num(num_array[1])

    new_node = Node()
    new_node.left = left_node
    left_node.parent = new_node
    new_node.right = right_node
    right_node.parent = new_node

    last_left = left_node.get_last()
    first_right = right_node.get_first()

    if last_left is not None:
        last_left.next = first_right
    if first_right is not None:
        first_right.prev = last_left

    return new_node


def print_tree(node, level=0):
    if node.value is not None:
        print('\t'*level, node.value, " prev: ", "X" if node.prev is None else node.prev.value, ", next: ", "X" if node.next is None else node.next.value)
        return

    print('\t'*level, "[")
    print_tree(node.left, level+1)
    print_tree(node.right, level+1)
    print('\t'*level, "]")


file = fr.open_file_lines("example.txt")
numbers = []
for line in file:
    line_array = json.loads(line)
    numbers.append(parse_num(line_array))
