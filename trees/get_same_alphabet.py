from trees.bin_tree import Tree, print_tree
from trees.map import *
import random
import copy


def tree_generate(alphabet: str, node_number):
    tree = Tree(None)

    for i in range(node_number):
        rand_idx = random.randint(0, len(alphabet) - 1)
        tree.insert(MapNode(alphabet[rand_idx]))

    return tree


def merge_alphabet(left_node: MapNode, right_node: MapNode):
    if left_node is None:
        return right_node.alphabet
    if right_node is None:
        return left_node.alphabet

    for key in right_node.alphabet:
        if left_node.alphabet.get(key) is None:
            left_node.alphabet[key] = 0

    return left_node.alphabet


def print_alphabet(parent: MapNode):
    if parent.right is None and parent.left is None:
        print(parent.value, end='')
        print(parent.alphabet, end='')
    else:
        print(parent.value, end='')
        print(parent.alphabet, end='')
        print("( ", end='')

        if not (parent.left is None):
            print_alphabet(parent.left)

        print(" , ", end='')

        if not (parent.right is None):
            print_alphabet(parent.right)
        print(" )", end='')


def check_answer(way_map: Map, parent: MapNode):
    if not (way_map.map is None):
        inserted, way = way_map.insert(parent)

        if not inserted:
            print("way to the first node: " + parent.way)
            print("way to the second node: " + way)
            way_map.map = None


def write_alphabet(parent: MapNode, way_map: Map, cur_way: str):
    if parent.left is None and parent.right is None:
        parent.alphabet = dict([(parent.value, 0)])
        parent.way = cur_way
        check_answer(way_map, parent)
    else:
        if not(parent.left is None):
            write_alphabet(parent.left, way_map, cur_way + "L ")
        if not(parent.right is None):
            write_alphabet(parent.right, way_map, cur_way + "R ")

        parent.alphabet = merge_alphabet(copy.deepcopy(parent.left), copy.deepcopy(parent.right))

        if parent.alphabet.get(parent.value) is None:
            parent.alphabet[parent.value] = 0
        parent.way = cur_way
        check_answer(way_map, parent)


def main():
    tree = tree_generate("abcde", 10)
    print_tree(tree.root)
    print()

    way_map = Map()
    write_alphabet(tree.root, way_map, "root ")
    if not(way_map.map is None):
        print("no nodes with equal alphabet")
    print()

    print_alphabet(tree.root)


if __name__ == "__main__":
    main()
