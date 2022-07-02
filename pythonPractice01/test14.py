# 经典算法：变态青蛙跳“绝望升级版”
"""
算法分析：
设台阶数为n，对应的跳法数为f(n)
假设没有台阶时青蛙原地跳一下，则：
n = 0 -- f(0) = 1
n = 1 -- f(1) = 1
n = 2 -- f(2) = 2
n = 3 -- f(3) = f(2) + f(1) + f(0)
n = 4 -- f(4) = f(3) + f(2) + f(1) + f(0)
n = 5 -- f(5) = f(4) + f(3) + f(2) + f(1) + f(0)
...
n = n -- f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1) + f(0)
此递归公式无法直接看出等量关系，现对其采用数学归纳法进行化简：
f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(1) + f(0) -- 1式
现将所有的n = n - 1,得：
f(n-1) = f(n-2) + f(n-3) + f(n-4) + ... + f(1) + f(0) -- 2式
1式 - 2式：
f(n) - f(n-1) = f(n-1)
所以：
f(n) = 2 * f(n-1)
即：当台阶数为n时，对应跳法数f(n) = 2 * f(n-1)
"""
a = 1
b = 1
c = 2
d = 0
floor_num = int(input('请输入台阶数：'))
if floor_num == 0:
    d = a
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, d))
elif floor_num == 1:
    d = b
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, d))
elif floor_num == 2:
    d = c
    print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, d))
else:
    for i in range(floor_num - 2):
        d = 2 * c
        c = d
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, d))

"""
# 解法2：使用列表组织数据
# 初始值：当没有台阶时，假设青蛙原地跳一下
a = 1
# 当台阶数为1时，青蛙只有一种跳法
b = 1
# 当台阶数为2时，青蛙有两种跳法
c = 2
# 跳法数列表：对应台阶数得青蛙跳法数
l = [a,b,c]
floor_num = int(input('请输入台阶数：'))
if floor_num == 0:
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, a))
elif floor_num == 1:
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, b))
elif floor_num == 2:
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, c))
else:
# 实现递归计算台阶数，每计算一个结果将计算顺序后移用于下一次计算
for i in range(floor_num - 2):
d = 2 * c
c = d
l.append(d)
print('青蛙跳上一个{}级台阶共计{}种跳法'.format(floor_num, l[-1]))
"""
