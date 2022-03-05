# Q3: 按相反顺序输出列表 ['one', 'two', 'three']的值
# 第一种做法：
l1 = ['one','two','three']
for i in range(1,len(l1)+1):
    print(l1[-i])

# 第二种做法：
l2 = l1[::-1]
for i in l2:
    print(i)

# 第三种做法：reversed 和range 函数类似，生成的是迭代器，不直接返回list表
for i in reversed(l1):
    print(i)

# 第四种做法:
l1.reverse() # 直接倒序，返回至自身
for i in l1:
    print(i)
