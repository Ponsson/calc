import math
MAX_VALUE = 10000



def check_coef(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        raise ValueError("значение вне допустимого диапазона")
    if a == 0 and b == 0:
        raise ValueError("уравнение не существует")
def solve(a,b,c):
    if a == 0:
        if b != 0:  
            x = -c // b
            return 'линейное', None, [x] 
    else:
        d = b**2 - 4*a*c
        if d < 0:
            return 'квадратное', None, []
        elif d == 0:
            x = -b // (2*a)
            return 'квадратное', d, [x]
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            return 'квадратное', d, [x1, x2] 