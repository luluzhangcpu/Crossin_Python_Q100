# Q57: 判断101-200之间有多少个素数，并输出所有素数
l1 = []
cnt = 0
for i in range(101,201):
    c = 0
    for j in range(2,i):
        if i % j == 0:
            c = 2
            break
    if c == 0:
        l1.append(i)
        cnt += 1
print('101~200间，共有 %d 个素数' % cnt)
print('所有素数为:')
[print(i) for i in l1]
