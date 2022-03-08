# Q80: 勾股数 
# 所谓勾股数，一般是指能够构成直角三角形3条边的3个正整数（a,b,c)。即a2+b2=c2，a，b，cΣN。求1000以内的勾股数

# 为减少循环次数,假定 a <= b <= c
for i in range(1,1001):
    for j in range(i,1001):
        for k in range(j,1001):
            if i + j > k and  i * i + j * j == k * k:
                print(i,j,k)
