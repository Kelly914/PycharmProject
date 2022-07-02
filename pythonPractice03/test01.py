import random

# 准备代码：准备包含20个整数对象的序列
l = [random.randint(1, 50) for i in range(20)]
print('无序序列为：{}'.format(l))

'''
算法1：二分查找法
- 问题描述：针对一个已经有序的序列，现需要确定某一具体元素是否存在于该序列中，算法通过不断的以目标元素作为分割该有序序列的关键点，以
实现“不断的缩小目标元素的检索范围”，进而最终确定整个有序的序列中是否存在该元素。
- 要求：现通过编码实现该二分查找算法
'''
# 构造一个有序序列
l.sort()
print('当前有序序列：{}'.format(l))
target = int(input('请输入您要查找的数字>>>：'))
# 是否找到的结果，初始为False，如果找到，重置结果为True即可
is_in = False
for i in range(len(l)):
    # 定义子区间的左端点，初始索引为0
    left = 0
    # 定义子区间的右端点，初始索引为最后一个元素的索引值
    right = len(l) - 1
    # 当左端点一直小于右端点索引值，代表循环需要一直执行下去
    while left <= right:
        # 计算当前子区间中间点,以该中间点分割当前子区间为左右子区间
        mid = (left + right) // 2
        # 如果当前目标元素比中间值大，代表在右子区间
        if target > l[mid]:
            left = mid + 1
        # 如果当前目标元素比中间值小，代表在左子区间
        elif target < l[mid]:
            right = mid - 1
        else:
            # target = l[mid]，代表找到，重置结果值为True
            is_in = True
            break
    # 每一遍循环走完判断一下结果值，如果为True，代表已经找到，后续逻辑无需再执行
    if is_in:
        break
if is_in:
    print('找到了！{}在当前序列！'.format(target))
else:
    print('没找到！抱歉！')
