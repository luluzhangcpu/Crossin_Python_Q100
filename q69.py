# Q69: 回文数判断
# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同


def num(n):
    a = list(str(n))
    b = str(n)
    a.reverse()
    c = ''.join(a)
    if b == c:
        return ('%d 是回文数' % n)
    else:
        return ('%d 不是回文数' % n)
print(num(112211))
