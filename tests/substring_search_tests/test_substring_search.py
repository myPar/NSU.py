from typing import List
import sub_string_search
from sub_string_search import z_function_improve
from sub_string_search import z_function_simple
from tests.substring_search_tests.benchmark import benchmark, benchmark_morris
import matplotlib.pyplot as plt
import sub_string_morris_pratt
from tests.substring_search_tests.test_generator import generator


def get_substrings_indices(input_string: str, substring: str) -> List[int]:
    indices_list = []
    idx = 0

    while len(input_string) > 0:
        local_idx = input_string.find(substring)

        if local_idx == -1:
            break
        idx += local_idx    # substring index in start string
        indices_list.append(idx)
        input_string = input_string[local_idx + 1:]   # delete all symbols to idx, including first symbol of substring
        idx += 1

    return indices_list


def test_solution():
    generator(15, "ab", 20, 3, 1)   # input format - (line number, character library, string length, substring length, open type)
    generator(15, "cde", 10, 1, 2)
    generator(15, "fghi", 20, 3, 2)
    tests_data = open("tests_data")

    for line in tests_data.readlines():
        line = line.rstrip()
        input_string, substring = line.split(" ")
        assert get_substrings_indices(input_string, substring) == sub_string_search.get_substrings_indices(
            input_string, substring, z_function_simple)
        assert get_substrings_indices(input_string, substring) == sub_string_search.get_substrings_indices(
            input_string, substring, z_function_improve)
        assert get_substrings_indices(input_string, substring) == sub_string_morris_pratt.sub_string_search(
            input_string, substring)
    tests_data.close()


def main():
    test_solution()

    time_list1 = []
    time_list2 = []
    time_list3 = []
    tests_data = open("tests_data")
    line_number = 0

    for line in tests_data.readlines():
        line = line.rstrip()
        line_number += 1
        input_string, substring = line.split(" ")
        time_list1.append(benchmark(input_string, substring, z_function_simple))
        time_list2.append(benchmark(input_string, substring, z_function_improve))
        time_list3.append(benchmark_morris(input_string, substring))
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('tests')
    ax.set_ylabel('time ns')
    ax.grid()
    x_list = [i for i in range(1, line_number + 1)]

    ax.plot(x_list, time_list1, color='blue', label='simple z_function')
    ax.plot(x_list, time_list2, color='red', label='linear z_function')
    ax.plot(x_list, time_list3, color='green', label='morris-pratt')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

#pytest, unittest
