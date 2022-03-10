# Q30: 输入三角形三个边求计算三角形的面积
# 分析："三角形两边之和大于第三边，S=sqrt[p(p-a)(p-b)(p-c)]"
# 上述 p，为三角形半周长

from math import sqrt as math_sqrt
h = True
while h == True:
    a = float(input('请输入三角形的第1个边长:'))
    b = float(input('请输入三角形的第2个边长:'))
    c = float(input('请输入三角形的第3个边长:'))
    if a + b > c and a + c > b and b + c > a:
        print('恭喜你，构建了1个三角形！')
        p = (a + b + c) / 2 # p为三角形的半周长
        s = math_sqrt(p*(p-a)*(p-b)*(p-c)) # 三角形通用的面积公式：海伦公式
        print('该三角形面积为(保留2位小数):%.2f' % s)
        h = False
    else:
        print('抱歉，您未构建成功一个三角形，请重新输入数据！')
        h = True
