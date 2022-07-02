# 互不相同且无重复数字的三位数
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i * 100 + j * 10 + k)