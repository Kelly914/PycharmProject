# 经典算法：“猴子吃桃”
# 前一天的桃子数 = 2 * (当天桃子数 + 1)
x = 1
day = int(input("请输入天数："))
for i in range(day - 1, 0, -1):
    x = 2 * (x + 1)
print('{}天前原来共计有{}个桃子'.format(day, x))
