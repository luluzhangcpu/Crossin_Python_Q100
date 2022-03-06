# Q38: 统计中英文

s = input('请输入一行字符串:')
cnt = 0
snt = 0
dnt = 0
znt = 0
for i in s:
    if i.isalpha(): # 判断是否为 中英文字符；若仅为 英文,i.encode('utf-8').isalpha,为 True；若含有中文，False；
        cnt += 1
    elif i.isspace():
        snt += 1
    elif i.isdigit():
        dnt += 1
    else:
        znt += 1
print('该段字符串中，中英文字母个数为:%d 个，空格为:%d 个，数字为:%d 个，其他字符为:%d 个' % (cnt,snt,dnt,znt))
