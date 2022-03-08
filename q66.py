# Q66: 递归问题1  
# 利用递归方法求5!

def num(n):
    if n == 1:
        return 1
    else:
        return n * num(n-1)
print(num(5))
