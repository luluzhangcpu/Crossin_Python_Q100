# Q99: 分糖果 
# 10个小孩围城一圈分糖果，
# 老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，第5个小孩16块；
# 第6个小孩4块，第7个小孩10块，第8个小孩6块，第9个小孩14块，第10个小孩20块。
# 然后所有的小孩同时将手中的糖分一半给右边的小孩；糖块数为奇数的人可向老师要一块。
# 问经过这样几次后大家手中的糖的块数一样多？ 每人各有多少块糖？

# 第一种做法
import sys
sys.setrecursionlimit(5000)

def num(n):
    if n == 0:
        l = [10,2,8,22,16,4,10,6,14,20]
        return l
    else:
        l = num(n-1)
        l2 = [i/2 for i in l]
        l3 = [i/2 for i in l]
        l3 = [l3[-1]] + l3[:-1]
        l4 = list(map(lambda x,y:x+y,l2,l3))
        l5 = []
        for i in l4:
            if i % 2 != 0:
                i += 1
            l5.append(i)
        l = l5
        return l

for i in range(1000):
    a = num(i)
    b = set(a)
    if len(b) == 1:
        break
print(a)
print('经过 %d 次后，大家手中糖果一样多' % i)
print('每人各有 %d 块糖' % a[0])

# 第二种做法(更简便)
#    解题思路：
#    1.用列表存储当前小朋友的糖果数.
#    2.模拟糖果传递过程, (s[i-1] + s[i]) / 2
#    3.判断是否全相等

def fun():
    s = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]

    count = 0
    while not all([x == s[0] for x in s]):
        s = [(s[i - 1] + s[i]) / 2 for i in range(10)]
        s = [x + x % 2 for x in s]
        count += 1

    print(count, s)

fun()
