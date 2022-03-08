# Q63: 打印菱形图案
# 打印如下菱形图案
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

l1 = [i for i in range(1,9,2)]
l2 = [i for i in range(5,0,-2)]
l3 = l1 + l2
print(l3)
from math import fabs
for i in range(1,8):
    a = int(fabs(4 - i))
    print(a * ' ',end='')
    print('*' * l3[i-1],end='')
    print(a * ' ')
