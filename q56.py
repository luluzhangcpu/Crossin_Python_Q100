# Q56: 生兔子问题
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问第10个月的兔子总数为多少？ 
def tz(n):
    if n <= 2:
        return 1
    else:
        return tz(n-1) + tz(n-2)
print(tz(10))
