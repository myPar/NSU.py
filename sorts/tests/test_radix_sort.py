import copy
from sorts import radix_sort
from sorts.tests.list_generator import get_random_int_list


# tests with random lists with different length
test_list = get_random_int_list(1)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (radix_sort.solution(test_list) == copy_list)

test_list = get_random_int_list(3)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (radix_sort.solution(test_list) == copy_list)

test_list = get_random_int_list(5)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (radix_sort.solution(test_list) == copy_list)

test_list = get_random_int_list(20)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (radix_sort.solution(test_list) == copy_list)