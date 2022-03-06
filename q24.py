# Q24: 从控制台输入一段字符，统计各字符出现次数

# 输入：Crossin 的编程教室100题
# 输出：
# 字符：C, 出现次数：1。
# 字符：r, 出现次数：1。
# ...
s = str(input('请输入一段字符;'))
dict1 = {}
for i in s:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
for i,k in dict1.items():
    print('字符：%s,出现次数：%d。' % (i,k))
