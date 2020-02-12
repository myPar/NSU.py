def bubble_sort(input_list):
    was_swap = True             # "true" is two elements swapped while iteration

    while was_swap is True:
        was_swap = False

        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                was_swap = True

                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list


def solution(input_list):
    return bubble_sort(input_list)


def main():
    input_list = []
    str_list = input().split(" ")

    for i in range(len(str_list)):
        input_list.append(float(str_list[i]))

    print(solution(input_list))


if __name__ == "__main__":
    main()
