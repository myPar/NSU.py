import CheckDate

# tests for DayNumber solution
assert (CheckDate.solution(29, 2, 2001) == -1)  # incorrect input; 2001 is't leap year
assert (CheckDate.solution(33, 4, 1535) == -1)  # incorrect input; days number can not be more then days in the month
assert (CheckDate.solution(30, 2, 2077) == -1)  # incorrect input; days number can not be more then days in the month

assert (CheckDate.solution(29, 2, 4000) == 60)  # correct input
assert (CheckDate.solution(28, 3, 2004) == 88)  # correct input
assert (CheckDate.solution(14, 12, 2033) == 348)  # correct input
assert (CheckDate.solution(26, 4, 1251) == 116)  # correct input
