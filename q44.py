# Q44: 正整数分解质因数
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
