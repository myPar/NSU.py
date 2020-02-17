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
from sorts.benchmarks.time_benchmark import sorted_benchmark
import numpy as np
import matplotlib.pyplot as plt


def build_quadratic_sorts(max_arr_len: int, is_sorted: bool):
    time_dict = {"bubble_sort": [], "paste_sort": [], "choose_sort": []}

    for i in range(1, max_arr_len + 1):  # run benchmarks on arrays with different length, from 1 to max_arr_len
        input_arr = get_random_list(i)  # get list of length i with random elements

        copy1 = copy.copy(input_arr)
        copy2 = copy.copy(input_arr)
        copy3 = copy.copy(input_arr)

        if not is_sorted:
            time_dict["bubble_sort"].append(benchmark(bubble_sort.bubble_sort, copy1))
            time_dict["paste_sort"].append(benchmark(paste_sort.paste_sort, copy2))
            time_dict["choose_sort"].append(benchmark(choose_sort.choose_sort, copy3))
        else:
            time_dict["bubble_sort"].append(sorted_benchmark(bubble_sort.bubble_sort, copy1))
            time_dict["paste_sort"].append(sorted_benchmark(paste_sort.paste_sort, copy2))
            time_dict["choose_sort"].append(sorted_benchmark(choose_sort.choose_sort, copy3))

    x_list = np.arange(1, max_arr_len + 1, 1)
    y_list1 = time_dict["bubble_sort"]
    y_list2 = time_dict["paste_sort"]
    y_list3 = time_dict["choose_sort"]
    return x_list, [y_list1, y_list2, y_list3]


def build_NlogN_sorts(max_arr_len: int, is_sorted: bool):
    time_dict = {"quick_sort": [], "merge_sort": [], "heap_sort": []}

    for i in range(1, max_arr_len + 1):  # run benchmarks on arrays with different length, from 1 to max_arr_len
        input_arr = get_random_list(i)  # get list of length i with random elements

        copy1 = copy.copy(input_arr)
        copy2 = copy.copy(input_arr)
        copy3 = copy.copy(input_arr)
        if not is_sorted:
            time_dict["quick_sort"].append(benchmark(quick_sort.solution, copy1))
            time_dict["merge_sort"].append(benchmark(merge_sort.merge_sort, copy2))
            time_dict["heap_sort"].append(benchmark(heap_sort.heap_sort, copy3))
        else:
            time_dict["quick_sort"].append(sorted_benchmark(quick_sort.solution, copy1))
            time_dict["merge_sort"].append(sorted_benchmark(merge_sort.merge_sort, copy2))
            time_dict["heap_sort"].append(sorted_benchmark(heap_sort.heap_sort, copy3))

    x_list = np.arange(1, max_arr_len + 1, 1)
    y_list1 = time_dict["quick_sort"]
    y_list2 = time_dict["merge_sort"]
    y_list3 = time_dict["heap_sort"]
    return x_list, [y_list1, y_list2, y_list3]


def plot_graphics(x_list: object, y_lists: List[List[float]], colors, labels: List[object], axis):
    for i in range(len(y_lists)):
        axis.plot(x_list, y_lists[i], color=colors[i], label=labels[i])


def plot_builds(fig, max_array_length: int, colors: List[object], labels: List[object], build_sorts):
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlabel('array size')
    ax1.set_ylabel('time s')
    ax1.grid()
    ax1.set_title('on arbitrary arrays')
    print(ax1.title)

    cortege = build_sorts(max_array_length, False)
    plot_graphics(cortege[0], cortege[1], colors, labels, ax1)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlabel('array size')
    ax2.set_ylabel('time s')
    ax2.grid()
    ax2.set_title('on sorted arrays')
    print(ax2.title)

    cortege = build_sorts(max_array_length, True)
    plot_graphics(cortege[0], cortege[1], colors, labels, ax2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


def main():
    max_array_length = 100
    colors = ['red', 'green', 'blue']
    labels1 = ['quicksort', 'mergesort', 'heapsort']
    labels2 = ['bubblesort', 'pastesort', 'choosesort']

    fig1 = plt.figure()
    fig2 = plt.figure()

    plot_builds(fig1, max_array_length, colors, labels1, build_NlogN_sorts)
    plot_builds(fig2, max_array_length, colors, labels2, build_quadratic_sorts)
    plt.show()


if __name__ == "__main__":
    main()
