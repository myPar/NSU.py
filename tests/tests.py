# Day number tests:
import DayNumber
import Nod
import SimpleSort
import ArraySpec

# tests for dayNumber solution:
assert (DayNumber.solution(2020, 10, 14) == -1)  # incorrect input; input parameters: day, month, year
assert (DayNumber.solution(-5, 10, 14) == -1)  # incorrect input; year > 0, day > 1, 1 < month <= 12
assert (DayNumber.solution(12, 13, 2000) == -1)  # incorrect input; year > 0, day > 1, 1 < month <= 12
assert (DayNumber.solution(12, 10, -14) == -1)  # incorrect input; year > 0, day > 1, 1 < month <= 12
assert (DayNumber.solution(0, 0, 0) == -1)  # incorrect input; year > 0, day > 1, 1 < month <= 12

assert (DayNumber.solution(29, 2, 2001) == -1)  # incorrect input; 2001 is't leap year
assert (DayNumber.solution(33, 4, 1535) == -1)  # incorrect input; days number can not be more then days in the month
assert (DayNumber.solution(30, 2, 2077) == -1)  # incorrect input; days number can not be more then days in the month

assert (DayNumber.solution(29, 2, 4000) == 60)  # correct input
assert (DayNumber.solution(28, 3, 2004) == 88)  # correct input
assert (DayNumber.solution(14, 12, 2033) == 348)  # correct input
assert (DayNumber.solution(26, 4, 1251) == 116)  # correct input

# tests for Nod solution:
assert (Nod.solution(0, 0) == 0)
assert (Nod.solution(0, 1) == 1)
assert (Nod.solution(1342, 2134) == 22)
assert (Nod.solution(234, 128) == 2)
assert (Nod.solution(43, 137) == 1)
assert (Nod.solution(625, 225) == 25)

# tests for simpleSort solution
assert (SimpleSort.solution([2, 3, 1, 44, 5, 2, 6, 64, 34, 11]) == [1, 2, 2, 3, 5, 6, 11, 34, 44, 64])
assert (SimpleSort.solution([0]) == [0])
assert (SimpleSort.solution([2, 1, 3, 78, 30, 4, 0]) == [0, 1, 2, 3, 4, 30, 78])

# tests for ArraySpec (order: minimum element, maximum element, average, median, standard deviation, monotone elements number)
assert (ArraySpec.solution([10.3, 22.32, 11, 2, 3, 2.01, 33, 456, 22, 12.57]) == (2.0, 456.0, 57.42, 2.505, 140.411598682, 0, 3))
assert (ArraySpec.solution([0]) == (0.0, 0.0, 0.0, 0.0, None, 0, 1))        # list consist with one element
assert (ArraySpec.solution([]) == "the list is empty")


