from typing import List
import sub_string_search
from sub_string_search import z_function_improve
from sub_string_search import z_function_simple
from tests.substring_search_tests.benchmark import benchmark
import matplotlib.pyplot as plt


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
    tests_data = open("tests_data")

    for line in tests_data.readlines():
        line = line.rstrip()
        input_string, substring = line.split(" ")
        assert get_substrings_indices(input_string, substring) == sub_string_search.get_substrings_indices(
            input_string, substring, z_function_simple)
        assert (get_substrings_indices(input_string, substring) == sub_string_search.get_substrings_indices(
            input_string, substring, z_function_improve))
    tests_data.close()


def main():
    test_solution()

    time_list1 = []
    time_list2 = []
    tests_data = open("tests_data")
    line_number = 0

    for line in tests_data.readlines():
        line = line.rstrip()
        line_number += 1
        input_string, substring = line.split(" ")
        time_list1.append(benchmark(input_string, substring, z_function_simple))
        time_list2.append(benchmark(input_string, substring, z_function_improve))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel('tests')
    ax.set_ylabel('time ns')
    ax.grid()
    x_list = [i for i in range(1, line_number + 1)]

    ax.plot(x_list, time_list1, color='blue', label='simple z_function')
    ax.plot(x_list, time_list2, color='red', label='linear z_function')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

#pytest, unittest
