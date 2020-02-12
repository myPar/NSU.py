from typing import List


def fib_rec(number: int) -> int:
    if number == 1:
        return 1
    if number == 2:
        return 2
    return fib_rec(number - 1) + fib_rec(number - 2)


def fib_dynamic(number: int) -> int:
    fibonacci_list = [1, 1]

    for i in range(2, number + 1):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
    return fibonacci_list[len(fibonacci_list) - 1]


def solution(n: int) -> int:
    # return fib_rec(n)
    return fib_dynamic(n)


def main():
    n = int(input())
    print(solution(n))


if __name__ == "__main__":
    main()
