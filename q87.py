# Q87: 黑洞数
# 黑洞数又称陷阱数，是类具有奇特转换特性的整数。
# 任何一个数字不全相同的整数，经有限“重排求差”操作，总会得到某一个或一些数，这些数即为黑洞数。
# “重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
# 举个例子，3位数的黑洞数为495.简易推导过程：随便找个数，如297,3个位上的数从小到大和从大到小各排一次，为972和279，相减得693。
# 按上面做法再做一次，得到594，再做一次，得到495，之后反复都得到495。
# 验证4位数的黑洞数为6174

l = []
for i in range(1000,9999):
    if len(set(str(i))) == 4:
        l.append(i)

def num(n,b):
    for j in range(b):
        a = list(str(n))
        d = sorted(a)
        c = sorted(a,reverse=True)
        n1 = int(''.join(d))
        n2 = int(''.join(c))
        n = n2 - n1
    return n
c = 0
for j in l:
    if num(j,20) != 6174:
        print(j)
    else:
        c += 1
if c == len(l):
    print('4位数的黑洞数为 6174')
