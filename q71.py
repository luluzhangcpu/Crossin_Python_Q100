# Q71: 报 3问题 
# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

a = int(input('共有多少人(整数输入):'))
l1 = [i for i in range(1,a+1)]
def num(c,n,l1):
    l2 = l1
    l1 = []
    if len(l2) < 3:
        return l2
    else:
        for i in range(c,n+c):
            if i % 3 != 0:
                l1.append(l2[i-c])
                d = i % 3
        b = len(l1)
        l1 = [l1[-1]]+l1[:-1]
        c = d
        return num(c,b,l1)
print(num(1,a,l1))
