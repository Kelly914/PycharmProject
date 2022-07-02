# 字符串反序
s = input("请输入字符串：")
new_s = ' '
for i in range(len(s) - 1, -1, -1):
    new_s += s[i]
print('反序字符串为：{}'.format(new_s))

"""
# 方法一：切片
print(s[::-1])
# 方法二
b = list(s)
# reverse() 函数用于反向列表中元素。
b.reverse()
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
print(''.join(b))
# 方法3
s = input("请输入字符串：")
l = len(s) - 1
arr = []
while l >= 0:
    arr.append(s[l])
    l = l - 1
print(''.join(arr))
"""
