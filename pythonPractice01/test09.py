# 输出100以内的所有质数
# 方法1
# 10以内只有2、3、5、7是质数，当一个数同时不能被2、3、5、7整除，则这个数是质数
# 0和 1是合数
for i in range(0, 101):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 0 and i != 1:
        print(i)

# 方法2
# 循环嵌套若后一个数可以整除前一个数，说明不是质数，跳出循环
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            print('发现一个质数：{}'.format(i))
