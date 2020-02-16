import copy
from typing import List
from sorts import bubble_sort
from sorts import paste_sort
from sorts import choose_sort
from sorts import merge_sort
from sorts import heap_sort
from sorts import quick_sort
from sorts.tests.list_generator import get_random_list
from sorts.benchmarks.time_benchmark import benchmark
import numpy as np
import matplotlib.pyplot as plt


def build_quadratic_sorts(max_arr_len: int):
    time_dict = {"bubble_sort": [], "paste_sort": [], "choose_sort": []}

    for i in range(1, max_arr_len + 1):     # run benchmarks on arrays with different length, from 1 to max_arr_len
        input_arr = get_random_list(i)  # get list of length i with random elements

        copy1 = copy.copy(input_arr)
        copy2 = copy.copy(input_arr)
        copy3 = copy.copy(input_arr)

        time_dict["bubble_sort"].append(benchmark(bubble_sort.bubble_sort, copy1))
        time_dict["paste_sort"].append(benchmark(paste_sort.paste_sort, copy2))
        time_dict["choose_sort"].append(benchmark(choose_sort.choose_sort, copy3))
    x_list = np.arange(1, max_arr_len, 1)
    y_list1 = time_dict["bubble_sort"]
    y_list2 = time_dict["paste_sort"]
    y_list3 = time_dict["choose_sort"]

    colours = ['red', 'green', 'blue']


def main():
    build_quadratic_sorts(10)


if __name__ == "__main__":
    main()
