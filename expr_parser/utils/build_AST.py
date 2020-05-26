from expr_parser.class_src.standart_classes import *
from typing import List


# returns operator index in notation
# or throws an exception if there is no operator
def get_operator_idx(postfix_notation: List[AstNode]) -> int:
    i = 0
    for i in range(len(postfix_notation)):
        if postfix_notation[i].type == Type.OPERATOR \
                and postfix_notation[i].left is None:
            return i
    BuildAbstractSyntaxTreeException("incorrect expression, can not get an operator: disturbed "
                                     "correct operands/operators count", postfix_notation[i].position).throw(mode)


def build_AST(postfix_stack: List[AstNode]):
    while len(postfix_stack) > 1:
        operator_idx = get_operator_idx(postfix_stack)
        operator = postfix_stack[operator_idx]

        if operator_idx - 2 < 0:
            BuildAbstractSyntaxTreeException("incorrect expression: disturbed "
                                             "correct operands/operators count",
                                             operator.position).throw(mode)
        operator.left = postfix_stack.pop(operator_idx - 2)
        operator.right = postfix_stack.pop(operator_idx - 2)

        if operator.value == "/" and operator.right.value == "0":
            ZeroDivisionException("division by zero", operator.position).throw(mode)
    # empty notation
    if len(postfix_stack) == 0:
        return None
    else:
        # input notation consisted from one operator
        if postfix_stack[0].type == Type.OPERATOR and postfix_stack[0].left is None:
            BuildAbstractSyntaxTreeException("incorrect expression: disturbed "
                                             "correct operands/operators count",
                                             postfix_stack[0].position).throw(mode)
        # return AST root
        return postfix_stack.pop(0)


def print_AST(root: AstNode, offset: str):
    if root.type == Type.OPERATOR:
        print(offset, end='')
        print("OPERATOR['" + root.value + "']")
        print(offset, end='')
        print("left:")
        print_AST(root.left, offset + "  ")

        print(offset, end='')
        print("right:")
        print_AST(root.right, offset + "  ")
    else:
        if root.type == Type.OPERAND:
            print(offset, end='')
            print("OPERAND['" + root.value + "']")
            return
        if root.type == Type.IDENT:
            print(offset, end='')
            print("IDENT['" + root.value + "']")
            return
        assert False, "All nodes in AST should have OPERATOR, OPERAND or IDENT types\n"
