# Q91: 可逆素数
# 编写程序找出1 ~ 900之间的所有可逆素数
# 可逆素数是指一个素数的各位数值顺序颠倒后得到的数仍为素数，如113、311

def num(n):
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            return True

for i in range(2,901):
    a = str(i)
    b = a[::-1]
    a = int(b)
    if num(i) and num(a):
        print(i)
