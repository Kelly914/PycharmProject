# 将一个列表反序
l = [1, 2, 3]
new_l = []
for i in range(len(l) - 1, -1, -1):
    new_l.append(l[i])
print('反序之后的列表为：{}'.format(new_l))
