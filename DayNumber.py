def is_Leap(year: int) -> bool:
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


def sum_days(d, month, day):
    days = 0

    for key in d:
        if key < month:
            days += d[key]
        else:
            return days + day


def correct_input(day, month, year, day_dict):  # function checks for incorrect input
    if day < 1 or (month < 1 or month > 12) or year < 0:
        return False
    if day > day_dict.get(month):
        return False
    return True


def solution(day_number, m, y):  # function for call in tests
    if is_Leap(y):
        if correct_input(day_number, m, y, d_leap):
            return sum_days(d_leap, m, day_number)
        else:
            return -1
    else:
        if correct_input(day_number, m, y, d):
            return sum_days(d, m, day_number)
        else:
            return -1


d_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # leap year day dict
d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # simple year day dict


def main():
    inputStr = input().split(" ")
    data = int(inputStr[0])
    month = int(inputStr[1])
    year = int(inputStr[2])

    print(solution(data, month, year))


if __name__ == "__main__":
    main()
