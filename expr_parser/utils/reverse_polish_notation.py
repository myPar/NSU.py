from expr_parser.class_src.Exception import*
from expr_parser.class_src.standart_classes import AstNode, mode
from expr_parser.class_src.standart_classes import Type
from typing import List


# builds reverse polish notation
def build_notation(node_list: List[AstNode]) -> List[AstNode]:
    output_stack = []
    operation_stack = []
    parenthesis_count = 0

    while len(node_list) > 0:
        node = node_list.pop(0)

        if node.type == Type.OPERAND or node.type == Type.IDENT:
            output_stack.append(node)
        else:
            if node.type == Type.OPERATOR:

                while len(operation_stack) > 0:
                    last_idx = len(operation_stack) - 1

                    if operation_stack[last_idx].type == Type.OPEN_PARENTHESIS:
                        break
                    if node.get_priority() > operation_stack[last_idx].get_priority():
                        break
                    else:
                        output_stack.append(operation_stack.pop(last_idx))
                operation_stack.append(node)
            if node.type == Type.OPEN_PARENTHESIS:
                parenthesis_count += 1
                operation_stack.append(node)
            if node.type == Type.CLOSE_PARENTHESIS:
                parenthesis_count -= 1
                is_complete = False

                for i in range(len(operation_stack) - 1, -1, -1):
                    node = operation_stack.pop(i)
                    if node.type == Type.OPEN_PARENTHESIS:
                        is_complete = True
                        break
                    output_stack.append(node)
                if not is_complete:
                    ParenthesisBalanceException("disturbed parenthesis balance, complete expression with '('",
                                                node.position).throw(mode)
    if parenthesis_count != 0:
        # because exception with incomplete '(' was not threw so there are incomplete ')' in the expression
        # all remaining '(' are in the operation stack
        for i in range(len(operation_stack) - 1, -1, -1):
            if operation_stack[i].type == Type.OPEN_PARENTHESIS:
                ParenthesisBalanceException("disturbed parenthesis balance, complete expression with ')'",
                                            operation_stack[i].position).throw(mode)
        assert False, "OPEN_PARENTHESIS should be in the operation stack"    # '(' should be the operation stack
    # push remaining elements in the output stack
    if len(operation_stack) > 0:
        for i in range(len(operation_stack) - 1, -1, -1):
            output_stack.append(operation_stack.pop(i))
    return output_stack


def print_notation(notation: List[AstNode]):
    for node in notation:
        print(node.value, end=' ')
