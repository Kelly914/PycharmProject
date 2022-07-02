# 动态构成一个完整的字符串
new_str = ''
while True:
    s = input('请输入一个字符：')
    if s == ' ':
        new_str += ''
        break
    new_str += s
print('构造的字符串为：{}'.format(new_str))
