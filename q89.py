# Q89: 孪生素数
# 若两个素数之差为2，则这两个素数就是孪生素数。编写程序找出1 ~ 100之间的所有孪生素数

# 为减少循环，可假定 a < b
def num(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for a in range(1,99):
    for b in range(a+2,101):
        if num(a) and num(b) and b - a == 2:
            print(b,a)
