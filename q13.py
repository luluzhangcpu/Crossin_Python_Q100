# Q13: 输入数字，将3个偶数加入列表

l1 = []
h = 0
while h < 3:
    a = int(input('请输入1个整数:'))
    if a % 2 == 0:
        l1.append(a)
        h += 1
print(l1)
