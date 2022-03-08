# Q26: 统计 1到100 内质数之和

l1 = []
for i in range(2,101):
    cnt = 0
    for j in range(1,i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        l1.append(i)
print(sum(l1))
