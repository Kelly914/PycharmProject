# 动态生成一个列表
l = []
while True:
    num = int(input('请输入一个数字：'))
    l.append(num)
    if len(l) == 10:
        break
print('添加元素之后的列表为：{}'.format(l))
