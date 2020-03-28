from trees.bin_tree import*


def print_tree_levels(root: Node):
    queue = [root, "\n"]

    while True:
        element = queue.pop(0)

        if element == "\n" and len(queue) == 0:
            break

        if element == "\n":
            print()
            queue.append("\n")
        else:
            print(element.value, end=' ')

            if not(element.left is None):
                queue.append(element.left)
            if not(element.right is None):
                queue.append(element.right)


def main():
    tree = generate_tree(10, 10)
    print_tree(tree.root)
    print("\n")
    print_tree_levels(tree.root)


if __name__ == "__main__":
    main()
