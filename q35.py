# Q35: 输入某年某月某日，判断这一天是这一年的第几天?
# 分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天

from datetime import datetime
import calendar
a = str(input('请输入一个日期(格式如"2021-01-21"):'))
b = datetime.strptime(a,'%Y-%m-%d').date()
cnt = 0
if b.month == 1:
    print('这一天是这一年的第 %d 天' % (b.day))
else:
    cnt = 0
    for i in range(1,b.month):
        cnt += calendar.monthrange(b.year,i)[1]
    cnt += b.day
    print('这一天是这一年的第 %d 天' % cnt)
