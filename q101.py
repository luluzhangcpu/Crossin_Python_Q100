# Q101: 倒序整数

# 第一种做法
a = 12428745
b = 0
h = True
while h == True:
    if a // 10 != 0:
        b = b * 10 + (a % 10) * 10
        a = a // 10
        h = True
    else:
        b += a
        h = False
print(b)

# 第二种做法
a = 12428745
a = list(str(a))
b = []
for i in a[::-1]:
    b.append(i)
print(int(''.join(b)))
