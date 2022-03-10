# Q74: 数组排序
# 有一个已经排好序的数组。[1,4,6,9,13,16,19,28,40,100]。现随机生成输入一个数（1-150），要求按原来的规律将它插入数组中。

from random import randint
l1 = [1,4,6,9,13,16,19,28,40,100]
a = randint(1,150)
if a >= l1[-1]:
    l1.append(a)
else:
    for i in range(1,len(l1)):
        if a >= l1[i-1] and a <= l1[i]:
            b = i
    l1.insert(b,a)
print(l1)
