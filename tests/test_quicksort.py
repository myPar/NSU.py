import copy
import random
from typing import List
import QuickSort


def get_random_list(length: int) -> List[float]:    # generates random list with fixed length
    random_list = []

    for i in range(length):
        random_list.append(random.uniform(-10000, 10000))
    return random_list


# tests for quick sort solution
assert (QuickSort.solution([2, 3, 1, 44, 5, 2, 6, 64, 34, 11]) == [1, 2, 2, 3, 5, 6, 11, 34, 44, 64])
assert (QuickSort.solution([0]) == [0])
assert (QuickSort.solution([2, 1, 3, 78, 30, 4, 0]) == [0, 1, 2, 3, 4, 30, 78])
assert (QuickSort.solution([34.1, 43.5, 12, 31.234, 5, 4, 3.25, 1, 1]) == [1.0, 1.0, 3.25, 4.0, 5.0, 12, 31.234, 34.1,

                                                                           43.5])
# tests with random lists with different length
test_list = get_random_list(1)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (QuickSort.solution(test_list) == copy_list)

test_list = get_random_list(3)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (QuickSort.solution(test_list) == copy_list)

test_list = get_random_list(5)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (QuickSort.solution(test_list) == copy_list)

test_list = get_random_list(10)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (QuickSort.solution(test_list) == copy_list)


