# Q67: 递归问题2
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

def num(l):
    l = list(l)
    a = len(l)
    if a == 1:
        return l[0]
    else:
        b = l.pop()
        c = b + num(l)
        return c
print(num('tyrue'))
