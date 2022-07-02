# 经典算法“不死兔子”
a = 1
b = 1
c = 0
month = int(input('请输入月份：'))
for i in range(month - 2):
    c = a + b
    a = b
    b = c
print('一年后共计：{}只兔子'.format(c * 2))

'''
# 解法2：使用列表组织数据
# 初始值为1，即前两月只有1对兔子
a = 1
b = 1
/=
l = [a,b]
month = int(input('请输入月份：'))
# 递归循环逻辑：新值为前一个值+前两个值，随后整体后移一位进行下一次计算，且新值入列表
for i in range(month - 2):
c = a + b
a = b
b = c
l.append(c)
print('一年后共计：{}只兔子'.format(l[-1]))
'''

