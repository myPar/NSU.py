from trees.get_same_alphabet import *


def main():
    tree = Tree(None)
    tree.insert(MapNode("b"))
    tree.insert(MapNode("c"))
    tree.insert(MapNode("b"))

    print_tree(tree.root)
    print()
    way_map = Map()
    write_alphabet(tree.root, way_map, "root ")
    print()
    if not(way_map.map is None):
        print("no nodes with equal alphabet")

    tree = Tree(None)
    tree.insert(MapNode("d"))
    tree.insert(MapNode("e"))
    tree.insert(MapNode("d"))
    tree.insert(MapNode("f"))

    print_tree(tree.root)
    print()
    way_map = Map()
    write_alphabet(tree.root, way_map, "root ")
    print()
    if not(way_map.map is None):
        print("no nodes with equal alphabet")

    node1 = MapNode("d")
    node2 = MapNode("b")
    node3 = MapNode("a")
    node4 = MapNode("c")
    node5 = MapNode("a")
    node6 = MapNode("c")
    node7 = MapNode("b")

    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.left = node6
    node5.right = node7

    print_tree(node1)
    print()
    way_map = Map()
    write_alphabet(node1, way_map, "root ")
    print()
    if not(way_map.map is None):
        print("no nodes with equal alphabet")

    tree = Tree(None)
    tree.insert(MapNode("d"))
    tree.insert(MapNode("b"))
    tree.insert(MapNode("k"))
    tree.insert(MapNode("e"))

    print_tree(tree.root)
    print()
    way_map = Map()
    write_alphabet(tree.root, way_map, "root ")
    if not(way_map.map is None):
        print("no nodes with equal alphabet")


if __name__ == "__main__":
    main()
