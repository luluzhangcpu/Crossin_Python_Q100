# Q47: 计算数字列表被最大数与最小数之差
# 定义一个数字列表 [2,4,1,2]，并计算列表元素最大数与最小数之差

# 第一种做法
from functools import reduce
a = reduce(lambda x,y:x if x >= y else y,[2,4,1,2])
b = reduce(lambda x,y:x if x <= y else y,[2,4,1,2])
print(a-b)

# 第二种做法
max1 = max([2,4,1,2])
min1 = min([2,4,1,2])
print(max1 - min1)
