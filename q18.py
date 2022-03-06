# Q18: 统计 1 到 100 能被3整除数之和

# 第一种做法
cnt = 0
for i in range(1,101):
    if i % 3 == 0:
        cnt += i
print(cnt)

# 第二种做法
print(sum([i for i in range(1,101) if (i % 3) == 0]))
