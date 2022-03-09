# Q95: 哥德巴赫猜想 
# 哥德巴赫猜想的证明是一个世界性的数学难题，至今未能完全解决。
# 所谓哥德巴赫猜想是说任何一个大于2的偶数都能表示成为两个素数之和。
# 编写程序，验证指定范围内[6, 100000]哥德巴赫猜想的正确性，也就是近似证明哥德巴赫猜想。

def num(n):
    if n == 2:
        return True
    else:
         for i in range(2,n):
             if n % i == 0:
                 break
         else:
            return True
l = []
for j in range(2,100000):
    if num(j):
        l.append(j)

l2 = []
for j in l:
    for i in l:
        c = i + j
        l2.append(c)
l2 = set(l2)

cnt = 0
for c in range(6,100001):
    if c % 2 == 0 and c in l2:
        cnt += 1

if cnt == (100000-6)/2 + 1:
    print('yes')
else:
    print('no')
