from typing import Dict


def is_Leap(year: int) -> bool:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def sum_days(day_dict: Dict[int, int], month: int, day_number: int) -> int:
    days = 0

    for key in day_dict:
        if key < month:
            days += day_dict[key]
        else:
            return days + day_number


def correct_input(day_number: int, month: int, year: int, day_dict: Dict[int, int]) -> bool:  # function checks for incorrect input
    if day_number < 1 or (month < 1 or month > 12) or year < 0:
        return False
    if day_number > day_dict[month]:
        return False
    return True


def check_date(day_number: int, month: int, year: int) -> int:  # function for call in tests
    d_leap = {1: 31,
              2: 29,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}  # leap year day dict
    d = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}  # simple year day dict

    if is_Leap(year):
        if correct_input(day_number, month, year, d_leap):
            return sum_days(d_leap, month, day_number)
        else:
            return -1
    else:
        if correct_input(day_number, month, year, d):
            return sum_days(d, month, day_number)
        else:
            return -1


def solution(day_number: int, month: int, year: int) -> int:
    return check_date(day_number, month, year)


def main():
    input_str = input().split(" ")
    data = int(input_str[0])
    month = int(input_str[1])
    year = int(input_str[2])

    print(solution(data, month, year))


if __name__ == "__main__":
    main()
