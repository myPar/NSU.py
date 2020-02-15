from typing import List


def choose_sort(input_list: List[float]) -> List[float]:
    for i in range(len(input_list)):
        min_element = input_list[i]
        min_ind = 0

        for j in range(i, len(input_list)):
            if input_list[j] <= min_element:
                min_element = input_list[j]  # update current minimum element
                min_ind = j  # update index
        input_list[i], input_list[min_ind] = input_list[min_ind], input_list[i]     # swap i'th element and minimum element

    return input_list


def main():
    input_list = list(map(float, input().split()))
    print(choose_sort(input_list))


if __name__ == "__main__":
    main()

