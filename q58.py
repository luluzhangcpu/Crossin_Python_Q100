# Q58: 水仙花数
# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
l1 = []
for i in range(100,1000):
    cnt = 0
    for j in str(i):
        cnt += int(j) ** 3
    if cnt == i:
        l1.append(i)
[print(i) for i in l1]
