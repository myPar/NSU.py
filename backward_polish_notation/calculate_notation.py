from backward_polish_notation.build_notation import *
from typing import List
from backward_polish_notation.Exception import *


def calculate(polish_notation: List[Node]) -> float:
    while len(polish_notation) > 1:
        op_idx = get_operation_idx(polish_notation)

        if op_idx < 2:  # less then two arguments before operation
            raise CalculateException("incorrect expression")
        operation = polish_notation.pop(op_idx)
        operand2 = polish_notation.pop(op_idx - 1)
        operand1 = polish_notation.pop(op_idx - 2)

        if not (operand1.type == "operand" and operand2.type == "operand"):
            raise CalculateException("incorrect expression")

        polish_notation.insert(op_idx - 2, operation.calculate(operand1.value, operand2.value))

    if not (polish_notation[0].type == "operand"):
        raise CalculateException("incorrect expression")
    return polish_notation[0].value


def get_operation_idx(stack: List[Node]) -> int:  # returns operation index
    has_op = False

    for i in range(len(stack)):
        if stack[i].type == "operation":
            return i

    if not has_op:
        raise CalculateException("incorrect expression")


def print_list(input_list: List[Node]):
    for i in input_list:
        print(i.value, end=' ')


def main():
    input_string = input()
    input_list = parse_string(input_string)
    print_list(input_list)
    print("\n")

    polish_notation = build(input_list)
    print_list(polish_notation)
    print("\n")

    print(calculate(polish_notation))


if __name__ == "__main__":
    main()
