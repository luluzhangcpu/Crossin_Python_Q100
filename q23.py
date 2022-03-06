# Q23: 从控制台输入一段字符，统计字符'b'出现次数

# 第一种做法
s = str(input('请输入一段英文字符串:'))
print(len([i for i in s if i == 'b']))

# 第二种做法
print(s.count('b'))
