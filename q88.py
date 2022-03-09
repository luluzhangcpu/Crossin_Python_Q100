# Q88: 3位反序数 
# 所谓反序数，即有这样成对的数，其特点是其中一个数的数字排列顺序完全颠倒过来，就变成另一个数;
# 如102和201，36和63等，简单的理解就是顺序相反的两个数，我们把这种成对的数互称为反序数。
# 反序数唯一不可能出现以0结尾的数。
# 一个3位数各位上的数字都不相同，它和它的反序数的乘积是280021，这个3位数应是多少？

from itertools import permutations
s = '9876543210'
l1 = list(permutations(s,3))
l = [''.join(i) for i in l1 if i[0] != '0' and i[-1] != '0']
a = [i for i in l if int(i[::-1]) * int(i) == 280021]
[print(int(i)) for i in a]
