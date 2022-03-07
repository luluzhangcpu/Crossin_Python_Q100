# Q52: 信息加密
def jm(n):
    n = str(n)
    n = n[::-1]
    c = []
    for i in n:
        c.append(str((int(i)+5) % 10))
    a = int(''.join(c))
    return a
print(jm(4567))
