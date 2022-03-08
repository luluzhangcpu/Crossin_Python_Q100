# Q70: 杨辉三角
# 打印出杨辉三角形（要求打印出10行如下图）
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

def num(cnt):
    if cnt == 1:
        l1 = [1]
        return l1
    elif cnt == 2:
        l1 = [1,1]
        return l1
    else:
        l1 = num(cnt-1)
        l2 = []
        for i in range(len(l1)-1):
            l2.append(l1[i] + l1[i+1])
        l2.insert(0,1)
        l2.append(1)
        return l2

for i in range(1,11):
    a = num(i)
    [print(j,end=' ') for j in a]
    print()
