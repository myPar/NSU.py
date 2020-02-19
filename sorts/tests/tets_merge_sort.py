import copy
from sorts import merge_sort
from sorts.tests.list_generator import get_random_list

# tests with random lists with different length
test_list = get_random_list(1)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (merge_sort.merge_sort(test_list) == copy_list)

test_list = get_random_list(3)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (merge_sort.merge_sort(test_list) == copy_list)

test_list = get_random_list(5)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (merge_sort.merge_sort(test_list) == copy_list)

test_list = get_random_list(10)
copy_list = copy.copy(test_list)
copy_list.sort()
assert (merge_sort.merge_sort(test_list) == copy_list)
