# Q42: 请你帮生成200个优惠券号码。优惠码的字符由26个英文字符（大小写）组成，每个优惠码有8位
from random import choice
l1 = [chr(i) for i in range(65,91)]
l2 = [chr(i) for i in range(97,123)]
l3 = l1 + l2
for i in range(200):
    l4 = []
    for j in range(8):
        a = choice(l3)
        l4.append(a)
    print(''.join(l4))
