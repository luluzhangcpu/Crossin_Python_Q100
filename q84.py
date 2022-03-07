# Q84: 年龄问题
# 王二、张三、李四、刘五年龄成一等差数列，他们四人的年龄相加是28，相乘是585。求以他们的年龄.
for i in range(1,8):
    l1 = {}
    for j in range(7):
        if 4*i + 6*j == 28 and i * (i+j) * (i + 2*j) * (i +3*j) == 585:
            l1['王二'] = i
            l1['张三'] = i + j
            l1['李四'] = i + 2*j
            l1['刘五'] = i + 3*j
            break
    if l1 != {}:
        break
for i,k in l1.items():
    print('%s 的年龄是 %d' % (i,k))
