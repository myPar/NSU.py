from typing import List


def prefix_function(input_string: str) -> List[int]:
    prefix_list = [0]*len(input_string)

    for i in range(1, len(prefix_list)):
        prefix_len = prefix_list[i - 1]

        while prefix_len > 0 and input_string[prefix_len] != input_string[i]:
            prefix_len = prefix_list[prefix_len - 1]
        if input_string[prefix_len] == input_string[i]:
            prefix_len += 1
        prefix_list[i] = prefix_len

    return prefix_list


def sub_string_search(input_string: str, substring: str) -> List[int]:
    prefix_list = prefix_function(substring + "#" + input_string)
    index_list = []

    for i in range(len(substring) + 1, len(prefix_list)):
        if prefix_list[i] == len(substring):
            index_list.append(i - 2 * len(substring))           # substring#...substring... i - last current substring index

    return index_list


def main():
    input_string, pattern = input().split()
    print(sub_string_search(input_string, pattern))


if __name__ == "__main__":
    main()