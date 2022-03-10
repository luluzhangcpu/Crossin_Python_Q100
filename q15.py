# Q15: 统计 1 到 100 之和

from functools import reduce
c = reduce(lambda x,y:x+y,[i for i in range(1,101)])
print(c)
