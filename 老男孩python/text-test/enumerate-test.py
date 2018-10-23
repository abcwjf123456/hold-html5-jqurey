# enumerate函数说明：
# 函数原型：enumerate(sequence, [start=0])
#
# 功能：将可循环序列sequence以start开始分别列出序列数据和数据下标
#
# 即对一个可遍历的数据对象(如列表、元组或字符串)，enumerate会将该数据对象组合为一个索引序列，同时列出数据和数据下标。

# import string#string模块具体看笔记
# s=string.ascii_lowercase
# print(list(enumerate(s)))#自己总结enumerate主要还是会在即对一个可遍历的数据对象(如列表、元组或字符串)加一个下标





# def xread_line(line):
#     return ((idx, int(val)) for idx, val in enumerate(line) if val != '0')
#
#
# print(xread_line('0001110101'))
#
# print(list(xread_line('0001110101')))



def hh(line):
    return ((var,int(linex) )for var,linex in enumerate(line) if linex>"5")

print(list(hh('5678')))#[(1, 6), (2, 7), (3, 8)]
