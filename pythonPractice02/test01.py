# 算法1 回文字符串
s = input("请输入一个字符串：")
left = 0
right = len(s) - 1
while left <= right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        break
if left > right:
    print("%s是回文字符串" % s)
else:
    print("%s不是回文字符串" % s)
"""
# 解法1
切片倒叙法
str1 = input('请输入一个字符串:')
if str1 == str1[::-1]:
    print('是一个回文字符串')
else:
    print('不是一个回文字符串')
    
# 解法2
# 解法2
new_strs = ''
for i in range(len(strs)-1,-1,-1):
    new_strs += strs[i]
    if new_strs == strs:
        print('是一个回文字符串')
    else:
        print('不是一个回文字符串')
"""
