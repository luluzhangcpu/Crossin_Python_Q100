# Q98: 肇事车辆 
# 有一个卡车司机肇事后想逃跑，但是被三个人看见了其车牌号，但是都没看全;
# 甲说：车牌的前两位是一样的；乙说：车牌的后两位一样的，但与前两位不一样;
# 丙说：车牌是一个数字的平方。
# 请编写一个程序计算该车牌号是多少（车牌号4位数）
from math import sqrt
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        else:
            a = str(i)+str(i)+str(j)+str(j)
            b = a
            c = sqrt(int(a))
            if c.is_integer():
                print(b)
