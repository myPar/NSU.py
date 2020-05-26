from typing import List
from expr_parser.class_src.standart_classes import*
from expr_parser.class_src.Exception import InfixFormatException


# this function check the correct writing of input infix notation
# because AST building pass notations like "ab*" so need an additional
# expression correctness checker
def check_notation(input_notation: List[AstNode]):
    length = len(input_notation)
    check_bound(input_notation, 0)
    check_bound(input_notation, length - 1)

    for idx in range(1, len(input_notation) - 1):
        node = input_notation[idx]
        left = input_notation[idx - 1]
        right = input_notation[idx + 1]

        if node.type == Type.OPERATOR:
            if left.type == Type.OPEN_PARENTHESIS or left.type == Type.OPERATOR:
                InfixFormatException("incorrect argument by left side of the OPERATOR", node.position).throw(mode)

            if right.type == Type.CLOSE_PARENTHESIS or right.type == Type.OPERATOR:
                InfixFormatException("incorrect argument by right side of the OPERATOR", node.position).throw(mode)
        if node.type == Type.OPERAND:
            pass


# method checks nodes at the expression bounds
def check_bound(input_notation: List[AstNode], idx: int):
    increment = 0
    if idx == 0:
        increment = 1
    if idx == len(input_notation) - 1:
        increment = -1
    assert increment != 0, "idx should be equal '0' or len(input_notation)\n"
    node = input_notation[idx]

    # operator is at the expression bound so throw an exception
    if node.type == Type.OPERATOR:
        InfixFormatException("OPERATOR have to has operands (including arguments in parenthesis) by both sides", node.position).throw(mode)
    # check operands and identifiers
    if node.type == Type.OPERAND or node.type == Type.IDENT:
        if input_notation[idx + increment].type != Type.OPERATOR:
            InfixFormatException("Only OPERATOR can be near OPERAND or IDENT", node.position).throw(mode)
    # check '(' at right bound of the expression
    if node.type == Type.OPEN_PARENTHESIS:
        if increment < 0:
            InfixFormatException("OPEN_PARENTHESIS can't be by right side of the expression", node.position).throw(mode)
    # check ')' at left bound of the expression
    if node.type == Type.CLOSE_PARENTHESIS:
        if increment > 0:
            InfixFormatException("CLOSE_PARENTHESIS can't be by left side of the expression", node.position).throw(mode)
