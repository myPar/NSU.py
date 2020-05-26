from trees.bin_tree import Node


class MapNode(Node):
    def __init__(self, value: str):
        Node.__init__(self, value)
        self.alphabet = None
        self.way = ""


class Map(object):
    def __init__(self):
        self.map = dict()

    def insert(self, node: MapNode):
        str_alphabet = "".join(list(node.alphabet))
        lex_alphabet = ""

        for i in range(len(str_alphabet)):
            lex_alphabet = insert_lex(lex_alphabet, str_alphabet[i])

        for key in self.map:
            if key == lex_alphabet:
                return False, self.map[key]

        self.map[lex_alphabet] = node.way
        return True, None


def insert_lex(string: str, symbol: str) -> str:
    for i in range(len(string)):
        if symbol <= string[i]:
            string = string[:i] + symbol + string[i:]
            return string

    return string + symbol
