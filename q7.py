# Q7: 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的*
from random import randint
for i in range(7):
    a = randint(1,50)
    print('*' * a)
