# Q11: 请使用 * 打印如下图形
# * * * * *
# *     *
# *   *
# * *
# *

for i in range(5):
    if i == 0:
        print('* ' * 5)
    elif i <= 3:
        print('*',end='')
        print((5 - (i - 1)*2)*' ',end='')
        print('*')
    else:
        print('*')
