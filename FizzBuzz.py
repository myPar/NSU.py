def fizz_buss(number: int) -> str:
    ret_str = ""

    for i in range(1, number + 1):
        count = 0
        if i % 3 == 0:
            ret_str += "Fizz"
            count += 1
        if i % 5 == 0:
            ret_str += "Buzz"
            count += 1
        if count == 0:
            ret_str += str(i)
        if i < number:          # don't add " " to the end of string
            ret_str += " "
    return ret_str


def solution(number: int):
    return fizz_buss(number)


def main():
    input_number = int(input())
    print(solution(input_number))


if __name__ == "__main__":
    main()

