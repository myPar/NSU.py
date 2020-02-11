import math

def average(list):
    number = 0
    for i in range(len(list)):
        number += list[i]
    return number/len(list)

def standard_deviation(list) -> float:
    number = 0
    aver = average(list)

    for i in range(len(list)):
        number += (list[i] - aver)**2
    return math.sqrt(number/(len(list) - 1))

def get_median(list):
    length = len(list)

    if length % 2 == 0:
        return (list[int(length/2) - 1] + list[int(length/2)])/2
    else:
        return list[int((length - 1) / 2)]

def get_sameNubers(list):
    prev_numb = list[0]
    number = 0
    max_number = -1

    for i in range(len(list)):
        if list[i] == prev_numb:
            number += 1
        if list[i] != prev_numb or i >= len(list) - 1:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = list[i]
    if max_number <= 1:
        return 0
    return max_number

def non_decr(list):
    prev_numb = list[0]
    number = 0
    max_number = -1

    for i in range(len(list)):
        if list[i] >= prev_numb:
            number += 1
        if i == len(list) - 1 or list[i] < prev_numb:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = list[i]
    return max_number

def non_incr(list):
    prev_numb = list[0]
    number = 0
    max_number = -1

    for i in range(len(list)):
        if list[i] <= prev_numb:
            number += 1
        if i == len(list) - 1 or list[i] > prev_numb:
            if number > max_number:
                max_number = number
            number = 1
        prev_numb = list[i]
    return max_number

def solution(list):
    if len(list) == 0:
        return "the list is empty"
    min_element = min(list)
    max_element = max(list)
    aver = round(average(list), 10)
    median = round(get_median(list), 10)
    if len(list) > 1:
        standard_dev = round(standard_deviation(list), 10)
    else:
        standard_dev = None
    equals = get_sameNubers(list)
    monotone = max(non_decr(list), non_incr(list))
    return(min_element, max_element, aver, median, standard_dev, equals, monotone)

def main():
    str_arr = input().split(" ")
    numbers = []

    for i in range(len(str_arr)):
        numbers.append(float(str_arr[i]))

    print(solution(numbers))

if __name__ == "__main__":
    main()
