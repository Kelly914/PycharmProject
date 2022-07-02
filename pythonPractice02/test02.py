# 字符串替换
s = input("请输入字符串：")
new_s = ' '
for i in s:
    if i == ' ':
        new_s += ','
    else:
        new_s += i
print('替换完成之后的字符串为：{}'.format(new_s))
# print(s.replace(' ', ','))
