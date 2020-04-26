from expr_parser.class_src.standart_classes import*
from expr_parser.utils.parse_string import*
from expr_parser.utils.reverse_polish_notation import*


def main():
    input_string = input()
    node_list = parse_string(input_string)
    for node in node_list:
        node.print()
    print()
    print_notation(build_notation(node_list))


if __name__ == "__main__":
    main()
