import time
from typing import List
from sorts import bubble_sort


def benchmark(sort_function, input_list: List[float]):  # default time benchmark
    start_time = time.perf_counter()
    sort_function(input_list)       # call of sort function
    end_time = time.perf_counter()
    return abs(end_time - start_time)    # return delta time in seconds


def standard_benchmark(input_list: List[float]):
    start_time = time.perf_counter()
    input_list.sort()
    end_time = time.perf_counter()
    return abs(end_time - start_time)
