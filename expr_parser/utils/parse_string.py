from expr_parser.class_src.standart_classes import *
from typing import List
import re


# wrote separate function of getting IDENT Token, to have
# possibility of float IDENT support in the future
def get_ident_value(input_string: str) -> str:
    i = 0
    length = len(input_string)

    while i < length and re.search(r'[0-9]', input_string[i]):
        i += 1
    return input_string[:i]


def parse_string(input_string: str) -> List[AstNode]:
    output_node_list = []
    pos = 0
    input_string = ''.join(input_string.split())
    token_ind = 0

    while token_ind < len(input_string):
        if re.search(r'[0-9]', input_string[token_ind]):    # check IDENT Token
            token_string_val = get_ident_value(input_string[token_ind:])
            token_ind += len(token_string_val)
        else:
            token_string_val = input_string[token_ind]
            token_ind += 1
        output_node_list.append(AstNode(token_string_val, pos))
        pos += 1

    return output_node_list


def main():
    input_string = input()
    node_list = parse_string(input_string)
    for node in node_list:
        node.print()


if __name__ == "__main__":
    main()
