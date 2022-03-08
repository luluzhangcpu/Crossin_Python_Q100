# Q25: 判断输入数字是否为质数问题】
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等）
# 换句话说就是该数除了1和它本身以外不再有其他的因数.
n = int(input('请输入一个整数:'))
a = n
if n == 1:
    print('%d 不是质数' % n)
elif n == 2:
    print('%d 是质数' % n)
else:
    for i in range(2,a):
        if n % i == 0:
            print('%d 不是质数' % n)
            break
    else:
        print('%d 是质数' % n)
