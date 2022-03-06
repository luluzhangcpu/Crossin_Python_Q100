# Q32: 请打印出 3*3 乘法口诀表
for i in range(1,4):
    for j in range(1, i + 1):
        print('%d X %d = %d' % (j,i,j*i))
