# Q90: 金蝉素数
# 这些数是由1,3,5,7,9这5个奇数字排列组成的5位素数;
# 同时去掉它的最高位与最低位数字后的3位数还是素数;
# 同时去掉它的高二位与低二位数字后的一位数还是素数;
# 因此人们把这些神秘的素数称为金蝉素数，喻意金蝉脱壳之后仍为美丽的金蝉。试求出石碑上的金蝉素数

from itertools import permutations
def num(n):
    if n == 2:
        return True
    else:
        for j in range(2,n):
            if n % j == 0:
                break
        else:
            return True
s = '13579'
l = list(permutations(s,5))
l2 = []
for i in l:
    j = ''.join(i)
    j = int(j)
    l2.append(j)

for j in l2:
    i = j
    if num(j):
        j = str(j)
        j = j[1:-1]
        j = int(j)
        if num(j):
            j = str(j)
            j = j[1:-1]
            j = int(j)
            if num(j):
                print(i)
