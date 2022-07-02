# 输出九九乘法表
n = int(input("请输入一个数："))
i = 1
while i <= n:
    j = 1
    while j <= i:  # i表示行数,j表示列数 行数=列数
        print('{} * {} = {}'.format(i, j, i * j), end=' ')
        j += 1
    print()
    i += 1
