# Q65: 求阶乘之和
# 求1+2!+3!+...+20!的和。n!=1×2×3×...×n

def num(n):
    c = 1
    for i in range(1,n+1):
        c = c * i
    return c

a = 0
for i in range(1,21):
    a += num(i)
print(a)
