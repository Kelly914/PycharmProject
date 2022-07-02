import random

# 准备代码：准备包含20个整数对象的序列
l = [random.randint(1, 50) for i in range(20)]
print('无序序列为：{}'.format(l))

'''
算法4：统计出现次数最多的元素
- 问题描述：现有一个无序序列，请统计出其中哪个元素出现的次数最大，并输出该元素的出现次数。
'''
dicts = {}
for i in l:
    if i not in dicts:
        dicts[i] = 1
    else:
        dicts[i] += 1
print('各元素的出现次数：{}'.format(dicts))
# 存放次数最大的键值
iIndex = ''
# 存放其对应的键名，键名即列表中出现过的元素
iMax = 0
# bug版找最大值：当最大次数存在多个元素时只能找到一个
for key in dicts:
    if dicts[key] > iMax:
        iIndex = key
        iMax = dicts[key]
# 改进版
# 遍历字典的值把每一个元素的出现次数单独摘出来为一个列表
max_num_list = []
for value in dicts.values():
    max_num_list.append(value)
print('个元素出现次数的集合为：{}'.format(max_num_list))
for index, key in enumerate(dicts):
    # 遍历元素次数列表，通过max获取最大值，然后判断：如果字典的某个键值对的值为该最大值，就输出这个键结果
    if dicts[key] == max(max_num_list):
        print('当前列表中第{}个出现次数最多的元素是：{}，其出现了：{}次'.format(index + 1, key, dicts[key]))
