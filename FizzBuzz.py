str = ""

for i in range(100):
    j = i + 1
    if (j % 3 == 0) and (j % 5 == 0):
        str += "FizzBuzz"
    else:
        if j % 3 == 0:
            str += "Fizz"
        else:
            if j % 5 == 0:
                str += "Buzz"
            else:
                str += j.__str__()
    str += " "

print(str)