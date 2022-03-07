# Q48: 任意输入两个整数求他们的最大公约数
from math import gcd as math_gcd

# 第一种做法
a = int(input('请输入第一个正整数:'))
b = int(input('请输入第二个正整数:'))
c = lambda x,y:x if x <= y else y
n = c(a,b)
d = []
for i in range(1,n + 1):
    if a % i == 0 and b % i == 0:
        d.append(i)
print(max(d))

# 第二种做法
c = a % b
while c != 0:
    a = b
    b = c
    c = a % b
print(b)

# 第三种做法
print(math_gcd(a,b))
