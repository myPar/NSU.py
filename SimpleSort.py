def sort(list):
    b = True

    while(b == True):
        b = False

        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                b = True

                number = list[i]
                list[i] = list[i + 1]
                list[i + 1] = number
    return list

def solution(list):
    return(sort(list))

def main():
    input_list = []
    str_list = input().split(" ")

    for i in range(len(str_list)):
        input_list.append(int(str_list[i]))

    print(solution(input_list))

if __name__ == "__main__":
    main()