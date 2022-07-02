import random

# 准备代码：准备包含20个整数对象的序列
l = [random.randint(1, 50) for i in range(20)]
print('无序序列为：{}'.format(l))

'''
算法2：二维矩阵的元素查找
- 问题描述：在一个矩阵中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请编写一个算法，输入符合题目要求的
一个矩阵和一个整数，判断矩阵中是否含有该整数。
'''
# 构造一个符合题目描述要求的二维矩阵
l_2d = [
    [x for x in range(1, 6)],
    [y for y in range(2, 7)],
    [z for z in range(3, 8)],
    [m for m in range(4, 9)]
]
target = int(input('请输入您要查找的数字>>>：'))
# 是否找到的结果集
is_in = False
# 行方向起始检索位置：0，即第一行，从上往下
row = 0
# 最大行数
maxrow = len(l) - 1
# 列方向起始检索位置：len(l_2d[0]) - 1,即最后一列，从右向左
col = len(l_2d[0]) - 1
try:
    # 当列数不断减小且行数不断增大，即从右上 - 左下查找，没有到达左下角顶点时，循环一直执行
    while col >= 0 and row <= maxrow:
        # 如果目标值大于当前值，说明在行方向上，目标值在当前值的下面行，则行数+1
        if target > l_2d[row][col]:
            row += 1
        # 如果目标值小于当前值，说明在列方向上，目标值在当前值的左边，则列数-1
        elif target < l_2d[row][col]:
            col -= 1
        else:
            is_in = True
        break
except Exception as e:
    pass
if is_in:
    print('找到了！{}在当前序列！'.format(target))
else:
    print('没找到！抱歉了！')