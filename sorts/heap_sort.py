from typing import List


def trickle_up(index: int, heap_array: List[float]):  # move node up in the pyramid
    node_value = heap_array[index]
    paren_ind = int((index - 1) / 2)

    while index > 0 and node_value > heap_array[paren_ind]:
        node_value = heap_array[index]

        heap_array[index] = heap_array[paren_ind]  # swap node and paren
        heap_array[paren_ind] = node_value

        index = paren_ind  # change current index on paren index
        paren_ind = int((index - 1) / 2)    # change paren index


def trickle_down(index: int, heap_array: List[float]):  # move node down from root in the pyramid

    while index < int(len(heap_array) / 2):  # while node have children
        node_value = heap_array[index]
        left_ind = index * 2 + 1
        right_ind = index * 2 + 2

        if right_ind < len(heap_array) and heap_array[left_ind] < heap_array[right_ind]:  # check consistence of right child; get current maximum child index
            max_child_ind = right_ind
        else:
            max_child_ind = left_ind

        if node_value < heap_array[max_child_ind]:  # swap node and child
            heap_array[index] = heap_array[max_child_ind]
            heap_array[max_child_ind] = node_value
        else:
            break
        index = max_child_ind


def insert(node: float, heap_array: List[float]):  # inserts new node in pyramid
    heap_array.append(node)
    trickle_up(len(heap_array) - 1, heap_array)  # move node up in the pyramid


def remove(heap_list: List[float]):  # remove root from the heap
    last_ind = len(heap_list) - 1
    heap_list[0] = heap_list[last_ind]  # replace root on last element
    heap_list.pop(last_ind)  # remove last element


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
