# Q44: 正整数分解质因数
# 问题描述：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n!=k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

l = []
def num(n):
    global l
    if n == 1:
        return l
    else:
        for i in range(2,n+1):
            if n % i == 0:
                l.append(str(i))
                return num(int(n/i))
a = int(input('请输入一个正整数:'))
c = num(a)

if len(c) == 0:
    print('1=1')
else:
    b = '*'.join(c)
    print('%d=%s' % (a,b))
