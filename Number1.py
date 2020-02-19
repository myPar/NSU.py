import math

def quad_eq(a:float, b:float, c: float):
    if a == 0:
        if b == 0:
            if c == 0:
                return "for all x"
            else:
                return "No decision"
        return -c/b

    d = b*b - 4*a*c

    if d < 0:
        return "No decision"
    if d == 0:
        return -b/2*a
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    return x1, x2

assert(quad_eq(1, 1, 3) == "No decision")             # d < 0
assert(quad_eq(2, 1, 1) == "No decision")             # d < 0
assert(quad_eq(0, 2, 1) == -0.5)                      # 2*x + 1 = 0
assert(quad_eq(0, 0, 0) == "for all x")               # 0 = 0 (correct for all x)
assert(quad_eq(2, 3, 1) == (-0.5, -1))                # 2*x^2 + 3*x + 1 = 0