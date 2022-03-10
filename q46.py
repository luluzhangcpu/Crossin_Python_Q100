# Q46: 计算列表元素之积
# 定义一个数字列表 [2,4,1,2]，并计算列表元素之积

from functools import reduce
a = reduce(lambda x,y:x*y,[2,4,1,2])
print(a)
