import random

# 准备代码：准备包含20个整数对象的序列
l = [random.randint(1, 50) for i in range(20)]
print('无序序列为：{}'.format(l))

'''
算法3：有序序列插入
- 问题描述：现有一个已经有序的序列，请编写一段代码，将一个新元素插入其中，并构成一个新的有序序列。
'''
# 升序排列
l.sort()
print('升序排列后的序列：{}'.format(l))
insert_num = int(input('请输入你要插入的数字>>>:'))
index = 0
for i in range(len(l)):
    if insert_num < l[0]:
        index = 0
        break
    elif insert_num > l[-1]:
        index = len(l)
        break
    elif insert_num < l[i]:
        index = i
        break
l.insert(index, insert_num)
print('插入新值后的新的升序序列为：{}'.format(l))
