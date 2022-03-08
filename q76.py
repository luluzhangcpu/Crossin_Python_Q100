# Q76: 输出 1 到 10000 之间的阿姆斯特朗数

for i in range(1,10001):
    s = str(i)
    a = len(s)
    if i == sum([int(j) ** a for j in s]):
        print(i)
