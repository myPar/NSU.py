from typing import List


def insertion_sort(input_list: List[float]) -> List[float]:
    if len(input_list) > 1:

        for i in range(1, len(input_list)):
            j = i

            while j > 0:
                if input_list[j] < input_list[j - 1]:
                    input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]  # swap two elements
                    j -= 1
                else:
                    break
    return input_list


def main():
    input_list = list(map(float, input().split()))
    print(insertion_sort(input_list))


if __name__ == "__main__":
    main()

