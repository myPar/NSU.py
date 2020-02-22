from typing import List
import numpy as np


def z_function_simple(input_string: str) -> List[int]:
    z_function = [0]

    for i in range(1, len(input_string)):
        j = 0

        while j + i <= len(input_string) - 1:
            if input_string[j] != input_string[i + j]:
                break
            j += 1
        z_function.append(j)
    return z_function


def get_list(length: int):
    output_list = []

    for i in range(length):
        output_list.append(0)
    return output_list


def z_function_improve(input_string: str) -> List[int]:
    z_function = get_list(len(input_string))
    left = 0
    right = 0

    for i in range(1, len(input_string)):
        z_function[i] = max(0, min(z_function[i - left], right - i))    # current z-block - [left-right]; z-block [i - left] is enclosed in current block, if his size is less or equal right - i

        while i + z_function[i] < len(input_string) and input_string[i + z_function[i]] == input_string[z_function[i]]:
            z_function[i] += 1
        if i + z_function[i] > right:       # if z-block is out of range of block [left-right], change left and right border on i and i + z_function[i]
            left = i
            right = i + z_function[i]
    return z_function


def main():
    input_string = input()
    print(z_function_improve(input_string))


if __name__ == "__main__":
    main()
