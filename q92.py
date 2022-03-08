# Q92: 回文素数判断
# 回文素数是指，对一个整数n从左向右和从右向左读结果值相同且是素数，即称为回文素数。
# 求不超过1000的回文素数


print(2)
print(3)
for i in range(4,1001):
    a = str(i)
    if a != a[::-1]:
        continue
    else:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
