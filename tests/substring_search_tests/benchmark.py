import time
from sub_string_search import get_substrings_indices
from sub_string_morris_pratt import sub_string_search


def benchmark(input_string: str, substring: str, z_function):
    start_time = time.perf_counter_ns()
    get_substrings_indices(input_string, substring, z_function)
    end_time = time.perf_counter_ns()
    return abs(end_time - start_time)


def benchmark_morris(input_string: str, substring: str):
    start_time = time.perf_counter_ns()
    sub_string_search(input_string, substring)
    end_time = time.perf_counter_ns()
    return abs(end_time - start_time)
