import copy
import math
from typing import List


def min_max(input_list: List[float]) -> (float, float):
    minimum = 1000000000000
    maximum = -1000000000000

    for i in range(len(input_list)):
        if input_list[i] > maximum:
            maximum = input_list[i]
        if input_list[i] < minimum:
            minimum = input_list[i]
    return minimum, maximum


def average(input_list: List[float]) -> float:
    number = 0
    for i in range(len(input_list)):
        number += input_list[i]
    return number / len(input_list)


def standard_deviation(input_list: List[float]) -> float:
    number = 0
    aver = average(input_list)

    for i in range(len(input_list)):
        number += (input_list[i] - aver) ** 2
    return math.sqrt(number / (len(input_list) - 1))


def get_median(input_list: List[float]) -> float:
    length = len(input_list)
    copy_list = copy.copy(input_list)  # make a copy because original list shouldn't be sorted
    copy_list.sort()

    if length % 2 == 0:
        return (copy_list[int(length / 2) - 1] + copy_list[int(length / 2)]) / 2
    else:
        return copy_list[int((length - 1) / 2)]


def get_sameNubers(input_list: List[float]) -> int:
    prev_numb = input_list[0]
    number = 0
    max_number = -1

    for i in range(len(input_list)):
        if input_list[i] == prev_numb:
            number += 1
        if input_list[i] != prev_numb or i >= len(input_list) - 1:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = input_list[i]

    return max_number


def non_decrease(input_list: List[float]) -> int:
    prev_numb = input_list[0]
    number = 0
    max_number = -1

    for i in range(len(input_list)):
        if input_list[i] >= prev_numb:
            number += 1
        if i == len(input_list) - 1 or input_list[i] < prev_numb:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = input_list[i]
    return max_number


def non_increase(input_list: List[float]) -> int:
    prev_numb = input_list[0]
    number = 0
    max_number = -1

    for i in range(len(input_list)):
        if input_list[i] <= prev_numb:
            number += 1
        if i == len(input_list) - 1 or input_list[i] > prev_numb:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = input_list[i]
    return max_number


def solution(input_list: List[float]) -> (float, float, float, float, float, int, int):
    if len(input_list) == 0:
        raise ValueError('empty list')  # throw exception if the list is empty
    min_element, max_element = min_max(input_list)
    aver = round(average(input_list), 10)
    median = round(get_median(input_list), 10)
    if len(input_list) > 1:
        standard_dev = round(standard_deviation(input_list), 10)
    else:
        standard_dev = None
    equals = get_sameNubers(input_list)
    monotone = max(non_decrease(input_list), non_increase(input_list))
    return min_element, max_element, aver, median, standard_dev, equals, monotone


def main():
    str_arr = input().split(" ")
    numbers = []

    for i in range(len(str_arr)):
        numbers.append(float(str_arr[i]))

    print(solution(numbers))


if __name__ == "__main__":
    main()
