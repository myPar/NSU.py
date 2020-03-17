import re
from typing import List
from backward_polish_notation.Exception import *


class Node(object):

    def __init__(self, node_type: str, value):
        self.type = node_type  # item types - (float value, operation, parenthesis)
        self.value = value

    def calculate(self, operand1: float, operand2: float) -> float:
        if self.value == '+':
            return operand1 + operand2
        if self.value == '-':
            return operand1 - operand2
        if self.value == '*':
            return operand1 * operand2
        if self.value == '/':
            if operand2 == 0:
                raise CalculateException("division by zero")
            return operand1 / operand2

    def get_priority(self):
        if self.value == '+' or self.value == '-':
            return 1
        if self.value == '*' or self.value == '/':
            return 2


def build(input_list: List[Node]) -> List[Node]:  # build notation function
    output_stack = []
    operation_stack = []
    parenthesis_count = 0

    while len(input_list) > 0:
        node = input_list.pop(0)

        if node.type == "operand":
            output_stack.append(node)
        else:
            if node.type == "operation":
                operation_stack.append(node)
                last_idx = len(operation_stack) - 1

                if last_idx > 0:        # check the priority
                    if node.get_priority() < operation_stack[last_idx - 1].get_priority():
                        output_stack.append(operation_stack.pop(last_idx - 1))
                operation_stack.append(node)
            else:
                if node.value == '(':
                    parenthesis_count += 1
                if node.value == ')':
                    parenthesis_count -= 1

                    is_complete = False

                    for i in range(len(operation_stack) - 1, 0, -1):    # push parenthesis body in the output stack
                        if operation_stack[i] == '(':
                            is_complete = True
                            operation_stack.pop(i)
                            break
                        else:
                            output_stack.append(operation_stack.pop(i))

                    if not is_complete:     # parenthesis balance disturbed
                        raise ParenthesisException("complete the expression by '('")

    if parenthesis_count != 0:      # parenthesis balance disturbed
        raise ParenthesisException("complete the expression by ')'")

    length = len(operation_stack)

    if length > 0:
        while length > 0:       # push remaining elements in the output stack
            output_stack.append(operation_stack.pop(length - 1))
            length -= 1

    return output_stack


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
                    raise SyntaxException("incorrect float number")
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
            raise SyntaxException("unacceptable input symbol")


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
