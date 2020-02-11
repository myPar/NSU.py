def nod(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return nod(a % b, b)
    if a < b:
        return nod(a, b % a)

def solution(a:int, b: int):
    return(nod(a, b))

def main():
    (a, b) = input().split(" ")
    a = int(a)
    b = int(b)
    print(solution(a, b))

if __name__ == "__main__":
    main()
