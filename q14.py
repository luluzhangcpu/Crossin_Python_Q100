# Q14: 输入整数，判断是否为偶数，是则加入列表，列表满三个元素则程序退出并按从小到大顺序输出

l1 = []
for i in range(3):
    h = True
    while h == True:
        a = int(input('请输入1个整数:'))
        if a % 2 == 0:
            l1.append(a)
            h = False
        else:
            h = True
l1.sort()
print(l1)
