# 计算闰年
x = int(input("请输入一个年份："))
if x % 400 == 0:
    print("{}年是闰年".format(x))
elif x % 4 == 0 and x % 100 != 0:
    print("{}年是闰年".format(x))
else:
    print("{}年不是闰年".format(x))
