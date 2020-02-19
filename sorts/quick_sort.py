from typing import List


def quick_sort(left_idx: int, right_idx: int, input_list: List[float]):
    if left_idx < right_idx:
        middle_idx = partion(left_idx, right_idx, input_list)
        quick_sort(left_idx, middle_idx, input_list)  # apply function for left part of list
        quick_sort(middle_idx + 1, right_idx, input_list)  # apply function for right part of list
    else:
        return


def swap(i: int, j: int, input_list: List[float]):
    input_list[i], input_list[j] = input_list[j], input_list[i]


def partion(left_idx: int, right_idx: int, input_list: List[float]) -> int:
    center = input_list[(left_idx + right_idx) // 2]
    i = left_idx
    j = right_idx

    while i <= j:
        while input_list[i] < center:  # if left element less then center element move index right
            i += 1
        while input_list[j] > center:  # if right element bigger then center move index left
            j -= 1
        if i >= j:
            break
        swap(i, j, input_list)
        i += 1  # increment indexes after swap
        j -= 1  #
    return j  # return index


def solution(input_list: List[float]):
    quick_sort(0, len(input_list) - 1, input_list)
    return input_list


def main():
    input_list = list(map(float, input().split()))
    print(solution(input_list))


if __name__ == "__main__":
    main()
