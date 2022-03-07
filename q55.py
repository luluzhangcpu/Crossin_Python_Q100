# Q55: 数字组合问题:有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少?

l1 = [1,2,3,4]
cnt = 0
c = []
l2 = []
for i in range(4):
    c.append(str(l1[i]))
    d = l1.pop(i)
    for j in range(3):
        c.append(str(l1[j]))
        b = l1.pop(j)
        for k in range(2):
            c.append(str(l1[k]))
            cnt += 1
            a = int(''.join(c))
            l2.append(a)
            c.pop()
        c.pop()
        l1.insert(j,b)
    c.pop()
    l1.insert(i,d)
print('能组成 %d 个互不相同且无重复数字的三位数' % cnt)
print('分别为：')
[print(i) for i in l2]
