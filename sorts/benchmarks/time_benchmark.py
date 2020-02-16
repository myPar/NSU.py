import time
from typing import List
from sorts import bubble_sort


def benchmark(sort_function, input_list: List[float]):  # default time benchmark
    start_time = time.perf_counter_ns()
    sort_function(input_list)       # call of sort function
    end_time = time.perf_counter_ns()
    return abs(end_time - start_time)      # return delta time


def back_sorted_benchmark(sort_function, input_list: List[float]):  # benchmark for reversed sorted arrays
    input_list.reverse()
    return benchmark(sort_function, input_list)
