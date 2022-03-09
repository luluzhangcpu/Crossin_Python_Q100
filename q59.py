# Q59: 完数 
# 一个数如果恰好等于它的因子（即除了自身以外的约数）之和;
# 这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

def num(n):
    if n == 1 or n == 2:
        return False
    else:
        s = 1
        for i in range(2,n):
            if n % i == 0:
                s += i
        if s == n:
            return True
        else:
            return False
for j in range(1,1001):
    if num(j):
        print(j)
