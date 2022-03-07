# Q49: 任意输入两个整数求他们的最小公倍数
from math import gcd as math_gcd

# 第一种做法
a = int(input('请输入第一个正整数:'))
b = int(input('请输入第二个正整数:'))
d = a
e = b
c = a % b
while c != 0:
    a = b
    b = c
    c = a % b
f = d * e / b
print(f)

# 第二种做法
c = math_gcd(d,e)
f = d * e / c
print(f)
