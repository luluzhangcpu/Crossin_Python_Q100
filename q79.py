# Q79: 相亲数 
# 220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284。
# 284的真因数之和为1+2+4+71+142=220。
# 毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。
# 求100000以内的相亲数

l = [i for i in range(3,100001)]
def num(n):
    cnt = 0
    if n == 1:
        return 0
    else:
        for i in range(1,n):
            if n % i == 0:
                cnt += i
        return cnt
l1 = []
for j in l:
    a = num(j)
    b = num(a)
    if a != j and b == j:
        l1.append((j,a))
        l.pop(l.index(a))
print(l1)
