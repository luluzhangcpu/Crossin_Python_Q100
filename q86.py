# Q86: 尾数前移
# 求一个自然数N，个位数是6，将6提到最前面所得数是N的4倍
import sys
sys.setrecursionlimit(30000)
def num(n):
    i = str(n)
    a = i[-1] + i[:-1]
    b = int(a)
    if b == 4 * n and i[-1] == '6':
        return n
    else:
        return num(n + 10)
c = num(16)
print(c)
