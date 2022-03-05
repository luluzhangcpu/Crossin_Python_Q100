# Q8: 按列表数据 [19,49,10,1],依次打印相同数量的 *

# 第一种做法
l1 = [19,49,10,1]
for i in l1:
    print('*' * i)

# 第二种做法
print([i for i in l1]) # 返回结果：[19,49,10,1]
[print(i) for i in l1] # 遍历 列表 l1
[print('*'* i) for i in l1]
