# Q29: 输出1000-2000之间的闰年
l1 = []
for i in range(1000,2001):
    if i % 100 == 0:
        if i % 400 == 0:
            l1.append(i)
    elif i % 4 == 0:
        l1.append(i)
print(l1)
