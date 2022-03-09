# Q61: 猴子吃桃问题
# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个;
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个;
# 以后每天早上都吃了前一天剩下的一半零一个;
# 到第10天早上想再吃时，见只剩下一个桃子了;
# 求第一天共摘了多少

# 第一种做法：
def num(n):
    for i in range(9):
        a = n
        if a <= 0 or a % 2 != 0:
            return False
        else:
            n = int(a / 2) - 1
    return n
for j in range(4,2000):
    if num(j):
        if num(j)== 1:
            print(j)
            break

# 第二种做法
x2 = 1
for day in range(9,0,-1):
    x1 = (x2 + 1) * 2
    x2 = x1
print(x1)
