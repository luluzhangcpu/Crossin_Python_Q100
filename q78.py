# Q78: 不重复的 3位数
# 0 ~ 9这10个数字，可以组成多少个没有重复数字的3位数？
# 比如 123、456 这种，但不包括 112, 333 这种

from itertools import permutations
s = str('9876543210')
c = list(permutations(s,3))
l1 = []
for i in c:
    if i[0] != '0':
        l1.append(i)
        print(i)
print(len(l1))
