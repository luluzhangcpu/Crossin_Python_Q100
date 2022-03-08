# Q64: 求分数序列之和
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

a = 2
b = 1
d = 0
l1 = []
for i in range(20):
    l1.append('%d / %d' % (a,b))
    c = a / b
    d += c
    e = a + b
    b = a
    a = e
print(l1)
print(d)
