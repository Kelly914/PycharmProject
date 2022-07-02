# 判断最大值
a = int(input("请输入一个数："))
b = int(input("请输入一个数："))
c = int(input("请输入一个数："))

print((a if a > c else c) if a > b else (b if b > c else c))
print(max(a, b, c))
