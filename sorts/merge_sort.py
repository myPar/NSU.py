from typing import List


def merge_sorted_arrays(list1: List[float], list2: List[float]):  # gives two sorted arrays on input and returns merged sorted array
    ind1 = 0  # current index in list1
    ind2 = 0  # current index in list2
    output_list = []

    while ind1 < len(list1) and ind2 < len(list2):
        if list1[ind1] <= list2[ind2]:
            output_list.append(list1[ind1])
            ind1 += 1
        else:
            output_list.append(list2[ind2])
            ind2 += 1
    if ind1 < len(list1):
        output_list += list1[ind1:]  # appending not added elements
    if ind2 < len(list2):
        output_list += list2[ind2:]  #
    return output_list


def merge_sort(input_list: List[float]) -> List[float]:
    if len(input_list) == 1:
        return input_list           # list with sie 1 is sorted yet
    else:
        mid_ind = int((len(input_list) - 1) / 2)
        left_list = merge_sort(input_list[0:mid_ind + 1])                   # get left sorted list
        right_list = merge_sort(input_list[mid_ind + 1:len(input_list)])    # get right sorted list
        return merge_sorted_arrays(left_list, right_list)                   # merge lists


def main():
    input_list = list(map(float, input().split()))
    print(merge_sort(input_list))


if __name__ == "__main__":
    main()
