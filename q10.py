# Q10: 请使用 * 打印如下图形
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(5):
    print(i * ' ',end='')
    print((5-i) * '* ')
