import copy
from typing import List
from sorts import bubble_sort
from sorts import insertion_sort
from sorts import selection_sort
from sorts import merge_sort
from sorts import heap_sort
from sorts import quick_sort
from sorts.tests.list_generator import get_random_list
from sorts.benchmarks.time_benchmark import benchmark
from sorts.benchmarks.time_benchmark import standard_benchmark
import numpy as np
import matplotlib.pyplot as plt


def build_quadratic_sorts(max_arr_len: int, is_sorted: bool):
    time_dict = {"bubble_sort": [], "insertion_sort": [], "selection_sort": [], "standard_sort": []}
    size_list = np.arange(1, max_arr_len + 1, 10)

    for val in size_list:  # run benchmarks on arrays with different length, from 1 to max_arr_len
        input_arr = get_random_list(val)  # get list of length i with random elements

        if not is_sorted:
            time_dict["bubble_sort"].append(benchmark(bubble_sort.bubble_sort, copy.copy(input_arr)))
            time_dict["insertion_sort"].append(benchmark(insertion_sort.insertion_sort, copy.copy(input_arr)))
            time_dict["selection_sort"].append(benchmark(selection_sort.selection_sort, copy.copy(input_arr)))
            time_dict["standard_sort"].append(standard_benchmark(copy.copy(input_arr)))
        else:
            time_dict["bubble_sort"].append(benchmark(bubble_sort.bubble_sort, sorted(copy.copy(input_arr))))
            time_dict["insertion_sort"].append(benchmark(insertion_sort.insertion_sort, sorted(copy.copy(input_arr))))
            time_dict["selection_sort"].append(benchmark(selection_sort.selection_sort, sorted(copy.copy(input_arr))))
            time_dict["standard_sort"].append(standard_benchmark(sorted(copy.copy(input_arr))))

    time_list1 = time_dict["bubble_sort"]
    time_list2 = time_dict["insertion_sort"]
    time_list3 = time_dict["selection_sort"]
    time_list4 = time_dict["standard_sort"]

    return size_list, [time_list1, time_list2, time_list3, time_list4]


def build_NlogN_sorts(max_arr_len: int, is_sorted: bool):
    time_dict = {"quick_sort": [], "merge_sort": [], "heap_sort": [], "standard_sort": []}
    size_list = np.arange(1, max_arr_len + 1, 100)

    for val in size_list:  # run benchmarks on arrays with different length, from 1 to max_arr_len
        input_arr = get_random_list(val)  # get list of length i with random elements

        if not is_sorted:
            time_dict["quick_sort"].append(benchmark(quick_sort.solution, copy.copy(input_arr)))
            time_dict["merge_sort"].append(benchmark(merge_sort.merge_sort, copy.copy(input_arr)))
            time_dict["heap_sort"].append(benchmark(heap_sort.heap_sort, copy.copy(input_arr)))
            time_dict["standard_sort"].append(standard_benchmark(copy.copy(input_arr)))
        else:
            time_dict["quick_sort"].append(benchmark(quick_sort.solution, sorted(copy.copy(input_arr))))
            time_dict["merge_sort"].append(benchmark(merge_sort.merge_sort, sorted(copy.copy(input_arr))))
            time_dict["heap_sort"].append(benchmark(heap_sort.heap_sort, sorted(copy.copy(input_arr))))
            time_dict["standard_sort"].append(standard_benchmark(sorted(copy.copy(input_arr))))

    time_list1 = time_dict["quick_sort"]
    time_list2 = time_dict["merge_sort"]
    time_list3 = time_dict["heap_sort"]
    time_list4 = time_dict["standard_sort"]

    return size_list, [time_list1, time_list2, time_list3, time_list4]


def plot_builds(fig, max_array_length: int, colors: List[object], labels: List[object], build_sorts):
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlabel('array size')
    ax1.set_ylabel('time s')
    ax1.grid()
    ax1.set_title('on arbitrary arrays')

    cortege = build_sorts(max_array_length, False)      # cortege[0] - size_list, cortege[1] - time_list

    for i in range(len(cortege[1])):
        ax1.plot(cortege[0], cortege[1][i], color=colors[i], label=labels[i])

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlabel('array size')
    ax2.set_ylabel('time s')
    ax2.grid()
    ax2.set_title('on sorted arrays')

    cortege = build_sorts(max_array_length, True)

    for i in range(len(cortege[1])):
        ax2.plot(cortege[0], cortege[1][i], color=colors[i], label=labels[i])
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


def main():
    max_array_length = 10000
    colors = ['red', 'green', 'blue', 'black']
    labels1 = ['quicksort', 'mergesort', 'heapsort', 'standardsort']
    labels2 = ['bubblesort', 'insertionsort', 'selectionsort', 'standardsort']

    fig1 = plt.figure()
#    fig2 = plt.figure()

    plot_builds(fig1, max_array_length, colors, labels1, build_NlogN_sorts)
#    plot_builds(fig2, max_array_length, colors, labels2, build_quadratic_sorts)
    plt.show()


if __name__ == "__main__":
    main()
