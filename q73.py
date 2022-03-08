# Q73: 奇数组合问题 
# 求 0~7 这 8 个数字所能组成的奇数个数。
# 数字可不全用，但不可重复
# 比如：
# 1、3、5、7、21、31、13.....10234567
# ……

from itertools import permutations # 列表的排列方法(有次序）
from itertools import combinations # 列表的组合方法(无次序)

# 第一种做法
cnt = 0
s = 76543210
s = str(s)
for i in range(1,76543210):
    a = str(i)
    b = set(a)
    c = True
    for x in a:
        if x not in s:
            c = False
            break
    if c == True and i % 2 != 0 and len(a) == len(b):
        cnt += 1
print(cnt)
