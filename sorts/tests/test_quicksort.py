import copy
from sorts import quick_sort
from sorts.tests.list_generator import get_random_list


# tests for quick sort solution
assert (quick_sort.solution([2, 3, 1, 44, 5, 2, 6, 64, 34, 11]) == [1, 2, 2, 3, 5, 6, 11, 34, 44, 64])
assert (quick_sort.solution([0]) == [0])
assert (quick_sort.solution([2, 1, 3, 78, 30, 4, 0]) == [0, 1, 2, 3, 4, 30, 78])
assert (quick_sort.solution([34.1, 43.5, 12, 31.234, 5, 4, 3.25, 1, 1]) == [1.0, 1.0, 3.25, 4.0, 5.0, 12, 31.234, 34.1,

                                                                            43.5])
# tests with random lists with different length
test_list = get_random_list(1)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (quick_sort.solution(test_list) == copy_list)

test_list = get_random_list(3)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (quick_sort.solution(test_list) == copy_list)

test_list = get_random_list(5)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (quick_sort.solution(test_list) == copy_list)

test_list = get_random_list(10)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (quick_sort.solution(test_list) == copy_list)


