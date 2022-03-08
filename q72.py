# Q72: 猴子分桃 
# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份;
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

import sys
sys.setrecursionlimit(30000)

def hz(tz,cnt):
    a = tz
    while cnt < 6:
        if tz <= 0:
            break
        elif tz % 5 != 1:
            break
        else:
            tz = int((tz - 1) / 5 * 4)
            cnt += 1
    if cnt != 6 or tz <= 0:
        return hz(a+1,1)
    else:
        return a
print(hz(1,1))
