# 分解质因数
# n = int(input("请输入一个数："))
# ls = []
# i = 2
# while i <= n:
#     x = n % i
#     if x == 0:
#         ls.append(i)
#         n = n / i
#     else:
#         i = i + 1
# print(ls)


n = num = int(input("请输入一个数字："))
l = []
for i in range(num // 2 + 1):
    for j in range(2, n):
        if n % j == 0:
            l.append(j)
            n //= j
            break
if len(l) == 0:
    print('没有质因数！')
else:
    l.append(n)
print('{} = {}'.format(num, l[0]), end=' ')
for x in range(1, len(l)):
    print('* {}'.format(l[x]), end=' ')
