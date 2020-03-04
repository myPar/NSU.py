import re
from typing import List


class Node(object):

    def __init__(self, node_type: str, value):
        self.type = node_type  # item types - (float value, operation, parenthesis)
        self.value = value

    def calculate(self, operand1: float, operand2: float) -> float:
        if self == '+':
            return operand1 + operand2
        if self == '-':
            return operand1 - operand2
        if self == '*':
            return operand1 * operand2
        if self == '/':
            return operand1 / operand2


def build():  # build notation function
    pass


def get_float_value(input_string: str) -> float:
    has_point = False
    number = ""

    for i in range(len(input_string)):
        ch = input_string[i]
        match = re.search(r'[0-9]', ch)

        if match:   # numeral
            number += ch
        else:

            if ch == ".":   # possible exceptions: two '.' in one number, '.' is the last symbol of the string, not number character after '.'
                if has_point or i >= len(input_string) - 1 or not(re.search(r'[0-9]', input_string[i + 1])):
                    print("incorrect float number")
                else:
                    number += ch
                    has_point = True
            else:
                break

    if not has_point:
        return int(number)  # integer number
    else:
        return float(number)


def get_node(input_string: str) -> Node:
    ch = input_string[0]
    match = re.search(r'[0-9]', ch)

    if match:  # float operand case
        value = get_float_value(input_string)
        return Node("operand", value)
    else:
        match = re.search(r'[\+\*\/\-\(\)]', ch)

        if match:
            if ch == "(" or ch == ")":  # parenthesis case
                return Node("parenthesis", ch)
            else:
                return Node("operation", ch)    # operation case
        else:
            print("unacceptable input symbol")


def parse_string(input_string: str) -> List[Node]:
    node_list = []
    input_string = ''.join(input_string.split())

    while len(input_string) > 0:
        node = get_node(input_string)
        node_list.append(node)

        input_string = input_string[len(str(node.value)):]  # cut node value from the string

    return node_list


def main():
    input_string = input()
    parse_string(input_string)


if __name__ == "__main__":
    main()
