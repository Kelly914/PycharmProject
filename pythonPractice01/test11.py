# 斐波那契数列
a = 0
b = 1
num = int(input("斐波那契数列元素的个数："))
print(a, b, end=',', sep=',')
for i in range(num - 2):
    c = a + b
    a = b
    b = c
    print(c, end=',')

# 初值0 和 1
# a = 0
# b = 1
# 斐波那契数列的列表，初值为0 和 1
# l = [a,b]
# num = int(input('请问需要几个数的斐波那契数列：'))
# 递归循环逻辑：新值为前一个值+前两个值，随后整体后移一位进行下一次计算，且新值入列表
# for i in range(num - 2):
# c = a + b
# a = b
# b = c
# l.append(c)
# print('生成的斐波那契数列为：{}'.format(l))
