# Q34: 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
from math import sqrt as math_sqrt

def num(n):
    if float.is_integer(math_sqrt((n + 100))):
        if float.is_integer(math_sqrt((n + 268))):
            return n
    else:
        return num(n + 1)
print(num(1))
