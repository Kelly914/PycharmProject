# 列表去重
l = [1,2,3,4,2,3,1,4,5,7,6,8]
print('初始列表为：{}'.format(l))
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)
print('去重之后的列表为：{}'.format(new_l))
