# Q12:输入3个整数a,b,c，按大小顺序输出

l1 = []
for i in range(3):
    a = int(input('请输入1个整数：'))
    l1.append(a)
l1.sort()
print(l1)
