# Q96: 等差素数数列 
# 类似7、37、67、97、107、137、167、197，这样由素数组成的等差数列叫做等差素数数列。
# 编程找出100以内的等差素数数列

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
for j in range(2,100):
    if num(j):
        l.append(j)
print(l)
cnt = 0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        l2 = [l[i],l[j]]
        for k in range(1,len(l)-j):
            a = l[i] + (k+1) * (l[j]-l[i])
            if a in l and len(l2)-1 == k:
                l2.append(a)
        if len(l2) >= 3:
            print(l2)
        l2 = []
