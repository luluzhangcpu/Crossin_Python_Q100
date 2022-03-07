# Q53: 构建斐波那契数列，求解第n个斐波那契数
def fnb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fnb(n-1) + fnb(n-2)
print(fnb(4))
