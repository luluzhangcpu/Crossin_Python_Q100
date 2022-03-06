# Q20: 输入数字，如果平方运算后小于 50 则退出

h = True
while h == True:
    a = float(input('请输入1个数字:'))
    if a * a < 50:
        h = False
    else:
        h = True
