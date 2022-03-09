# Q62: 乒乓球比赛 
# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，
# 乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单

from itertools import permutations
l = ['x','y','z']
l2 = ['a','b','c']
c = list(permutations(l,3))
for i in c:
    if i[0] != 'x' and (i[2] != 'x' and i[2] != 'z'):
        print(f'a 对应 {i[0]}，b 对应 {i[1]}，c 对应{i[2]}')
