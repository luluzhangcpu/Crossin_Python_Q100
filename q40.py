# Q40: 移除字符串指定位置字符
# 移除字符串中的指定位置字符,"Crossin 的编程教室" 中第八位空白符

# 第一种做法
s = 'Crossin 的编程教室'
a = s[:7] + s[8:]
print(a)

# 第二种做法
l1 = list(s)
l1.pop(7)
print(''.join(l1))
