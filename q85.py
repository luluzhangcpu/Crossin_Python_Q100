# Q85: 双色球
# 根据福利彩票双色球玩法规则，6个蓝色球，范围为1 ~ 33，不允许重复，1个红色球，范围为1 ~ 16，
# 自动生成6个蓝色球，1个红色球。

from random import choice
from random import sample
blue1 = [i for i in range(1,34)]
red1 = [i for i in range(1,17)]
print(sample(blue1,6))
print(choice(red1))
