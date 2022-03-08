# Q93: 平方回文素数
# 素数的平方是回文，比如11 * 11=121。求不超过1000的平方回文素数
l1 = []
for i in range(2,1000):
    s = str(i ** 2)
    s = list(s)
    s2 = list(reversed(s))
    if s == s2:
        l1.append(i)

l2 = []
for i in l1:
    if i == 2 or i == 3:
        l2.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            l2.append(i)
[print(i) for i in l2]
