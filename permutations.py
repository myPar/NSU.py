import copy
from typing import List


def print_list(two_dim_list: List[List[int]]):
    for one_dim_list in two_dim_list:
        print(one_dim_list)


def get_perm(perm_list: List[List[int]], pasting_number: int) -> List[List[int]]:   # insert number on all indices in
    output_list = []

    for i in range(len(perm_list)):
        for j in range(len(perm_list[i]) + 1):
            copy_list = copy.copy(perm_list[i])
            copy_list.insert(j, pasting_number)
            output_list.append(copy_list)
    return output_list


def permutation(n: int) -> List[List[int]]:  # returns all permutations from 0 to n - 1
    if n == 1:
        return [[0]]
    return get_perm(permutation(n - 1), n - 1)


def solution(n: int) -> List[List[int]]:
    return permutation(n)


def main():
    n = int(input())
    print_list(solution(n))


if __name__ == "__main__":
    main()
