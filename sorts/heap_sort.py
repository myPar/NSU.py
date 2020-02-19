from typing import List


def trickle_up(index: int, heap_array: List[float]):  # move node up in the pyramid
    node_value = heap_array[index]
    paren_idx = (index - 1) // 2

    while index > 0 and node_value > heap_array[paren_idx]:
        node_value = heap_array[index]

        heap_array[index] = heap_array[paren_idx]  # swap node and paren
        heap_array[paren_idx] = node_value

        index = paren_idx  # change current index on paren index
        paren_idx = (index - 1) // 2    # change paren index


def trickle_down(index: int, heap_array: List[float]):  # move node down from root in the pyramid

    while index < len(heap_array) // 2:  # while node have children
        node_value = heap_array[index]
        left_idx = index * 2 + 1
        right_idx = index * 2 + 2

        if right_idx < len(heap_array) and heap_array[left_idx] < heap_array[right_idx]:  # check consistence of right child; get current maximum child index
            max_child_idx = right_idx
        else:
            max_child_idx = left_idx

        if node_value < heap_array[max_child_idx]:  # swap node and child
            heap_array[index] = heap_array[max_child_idx]
            heap_array[max_child_idx] = node_value
        else:
            break
        index = max_child_idx


def insert(node: float, heap_array: List[float]):  # inserts new node in pyramid
    heap_array.append(node)
    trickle_up(len(heap_array) - 1, heap_array)  # move node up in the pyramid


def remove(heap_list: List[float]):  # remove root from the heap
    last_idx = len(heap_list) - 1
    heap_list[0] = heap_list[last_idx]  # replace root on last element
    heap_list.pop(last_idx)  # remove last element


def heap_sort(input_list: List[float]) -> List[float]:
    output_list = []
    heap_list = []

    for i in range(len(input_list)):
        insert(input_list[i], heap_list)

    while len(heap_list) > 0:
        output_list.insert(0, heap_list[0])
        remove(heap_list)
        trickle_down(0, heap_list)
    return output_list


def main():
    input_list = list(map(float, input().split()))
    print(heap_sort(input_list))


if __name__ == "__main__":
    main()
