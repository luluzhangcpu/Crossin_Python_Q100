# Q2: 按相反顺序输出列表 ['one', 'two', 'three']的值
# 第一种做法：
l1 = ['one','two','three']
for i in range(1,len(l1)+1):
    print(l1[-i])

# 第二种做法：
l2 = l1[::-1]
for i in l2:
    print(i)
