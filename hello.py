# -*- codeing = utf-8 -*-
# @Time :2021/10/18 20:08
# @Author :menglei
# @File :hello.py
# @Software: PyCharm

# print('hello world')
# name = 'TOM'
# print('我的名字是%s' % name)
# print(f'我的名字是{name}')
#
# # 输入密码
# password = input('请输入您的密码')
# print(f'您输入的密码是{password}')
# print(type(password))

# str1 = 'abcdefg'
# print(str1)
#
# print(str1[0])

# 切片 序列名[开始位置的下标：结束位置的下标：步长]

str1 = '0123456789'
#print(str1[2:5:1])  # 从2开始到5（不包含），步长为1

# print(str1[2:5])
# print(str1[:5]) # 01234
# print(str1[2:]) # 23456789
# print(str1[::-1]) # 如果步长为负数， 表示倒叙选取
# print(str1[-4:-1:]) # 678 下标-1表示最后一个数据，一次向前类推
# print(str1[-1]) # 678 下标-1表示最后一个数据

# 终极测试
print(str1[-1:-4:-1])

