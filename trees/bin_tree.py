import random


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, root: Node):
        self.root = root

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
        else:
            paste_node(node, self.root)


def paste_node(node: Node, parent: Node):
    if node.value < parent.value:
        if parent.left is None:
            parent.left = node
        else:
            paste_node(node, parent.left)
    if node.value >= parent.value:
        if parent.right is None:
            parent.right = node
        else:
            paste_node(node, parent.right)


def print_tree(parent: Node):
    if parent.right is None and parent.left is None:
        print(parent.value, end='')
        return
    else:
        print(str(parent.value) + "( ", end='')

        if not (parent.left is None):
            print_tree(parent.left)

        print(" , ", end='')

        if not (parent.right is None):
            print_tree(parent.right)
        print(" )", end='')


def generate_tree(node_number: int, span: int) -> Tree:
    tree = Tree(None)

    for i in range(node_number):
        value = random.randint(-span, span)
        node = Node(value)
        tree.insert(node)
    return tree


def main():
    tree = Tree(None)
    tree.insert(Node(10))
    tree.insert(Node(12))
    tree.insert(Node(9))
    tree.insert(Node(9))
    tree.insert(Node(8))
    tree.insert(Node(10))
    print_tree(tree.root)
    print()
    tree.insert(Node(10))
    tree.insert(Node(10))
    tree.insert(Node(10))
    print_tree(tree.root)


if __name__ == "__main__":
    main()
