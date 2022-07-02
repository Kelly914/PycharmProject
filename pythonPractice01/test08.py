# 计算一个数的阶乘
x = y = int(input("请输入一个数："))
for i in range(x - 1, 0, -1):
    y = x * i
print("{}! = {}".format(x, y))
