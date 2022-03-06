# Q25: 判断输入数字是否为质数
cnt = 0
n = int(input('请输入一个整数:'))
for i in range(1,n + 1):
    if n % i == 0:
        cnt += 1
if cnt == 1 or cnt == 2:
    print('%d 是质数' % n)
else:
    print('%d 不是质数' % n)
