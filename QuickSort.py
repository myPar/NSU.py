from typing import List


def quick_sort(left_ind: int, right_ind: int, input_list: List[float]):
    if left_ind < right_ind:  # while left index less then right index do recursion
        middle_ind = partion(left_ind, right_ind, input_list)
        quick_sort(left_ind, middle_ind, input_list)  # apply function for left part of list
        quick_sort(middle_ind + 1, right_ind, input_list)  # apply function for right part of list
    else:
        return


def swap(i: int, j: int, input_list: List[float]):
    input_list[i], input_list[j] = input_list[j], input_list[i]


# function swap elements by left and right side from central element if left element bigger then central and if right
# element less then central:
def partion(left_ind: int, right_ind: int, input_list: List[float]) -> int:
    center = input_list[int((left_ind + right_ind) / 2)]
    i = left_ind
    j = right_ind

    while i <= j:
        while input_list[i] < center:  # if left element less then center element move index right
            i += 1
        while input_list[j] > center:  # if right element bigger then center move index left
            j -= 1
        if i >= j:
            break
        swap(i, j, input_list)  # swap two elements
        i += 1  # increment indexes after swap
        j -= 1  #
    return j  # return index


def solution(input_list: List[float]):
    quick_sort(0, len(input_list) - 1, input_list)
    return input_list


def main():
    str_arr = input().split(" ")
    input_list = []

    for i in range(len(str_arr)):
        input_list.append(float(str_arr[i]))
    print(solution(input_list))


if __name__ == "__main__":
    main()
