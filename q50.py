# Q50: 字符串翻转:给定一个字符串如 "Crossin的编程教室"，然后将其翻转，逆序输出

# 第一种做法
a = input('请输入一段字符串:')
b = list(a)
b.reverse()
print(''.join(b))

# 第二种做法
b = []
for i in a[::-1]:
    b.append(i)
print(''.join(b))

# 第三种做法
print(a[::-1])
