from expr_parser.class_src.standart_classes import*
from expr_parser.utils.parse_string import*
from expr_parser.utils.reverse_polish_notation import*
from expr_parser.utils.build_AST import*


def main():
    input_string = input()
    node_list = parse_string(input_string)
    for node in node_list:
        node.print()
    print()
    notation_node_list = build_notation(node_list)
    print_notation(notation_node_list)
    print()

    root = build_AST(notation_node_list)
    print_AST(root, "")


if __name__ == "__main__":
    main()
