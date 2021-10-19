# -*- codeing = utf-8 -*-
# @Time :2021/10/19 9:02
# @Author :menglei
# @File :hm_09_字符串常用操作方法值修改非重点.py
# @Software: PyCharm

mystr = 'hello world and itcast and itheima and Python'
# 新建一个字符串，并将mystr字符串的第一个字母大写，其他的字母全部是小写，并返回该新建的字符串
new_str = mystr.capitalize()
print(new_str)

new_str = mystr.title()
print(new_str)

new_str = mystr.split('and')
print(new_str)

new_str = mystr.lower()
print(new_str)

new_str = mystr.upper()
print(new_str)