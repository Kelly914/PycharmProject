# 经典算法：“变态青蛙跳”
"""
算法分析：
设台阶数为n，对应的跳法数为f(n)
n = 1 -- f(1) = 1
n = 2 -- f(2) = 2
n = 3 -- f(3) = f(2) + f(1)
n = 4 -- f(4) = f(3) + f(2)
n = 5 -- f(5) = f(4) + f(3)
...
n = n -- f(n) = f(n-1) + f(n-2)
所以，n个台阶，青蛙的跳法数f(n) = f(n-1) + f(n-2)
"""

# 方法1
a = 1
b = 2
c = 0
floor_num = int(input('请输入台阶数：'))
if floor_num == 1:
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, a))
elif floor_num == 2:
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, b))
else:
    for i in range(floor_num - 2):
        c = a + b
        a = b
        b = c
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, c))


'''
# 解法2：使用列表组织数据
# 初始值：只有一个台阶时，青蛙跳法数为1
a = 1
# 初始值：只有两个台阶时，青蛙跳法数为2
b = 2
# 跳法数列表：对应台阶数得青蛙跳法数
l = [a,b]
floor_num = int(input('请输入台阶数：'))
if floor_num == 1:
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, a))
elif floor_num == 2:
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, b))
else:
# 实现递归计算台阶数，每计算一个结果将计算顺序后移用于下一次计算
for i in range(floor_num - 2):
c = a + b
a = b
b = c
l.append(c)
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num,l[-1]))
'''