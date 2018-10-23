def gg(num):
    return num>5
list1=[1,3,7,9,0]
name='vgvgvfgcgf 2018'
name1='sfgggh 21334.'
print(list(filter(gg,list1)))
print(list(filter(str.isalpha,name)))#过滤字母
print(list(filter(str.isdigit,name)))#过滤数字
print(list(filter(lambda x:x in '1234567890.',name1)))



# filter()函数用于过滤序列, 过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#
# filter()函数接收一个函数 func 和一个iterable(可以是list，字符串等)，这个函数 func 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，最后将返回 True 的元素放到新列表中。
#
#
#
# 语法
# filter(function, iterable)
#
#
#
# 参数
# function -- 判断函数。
#
# iterable -- 可迭代对象。
#
#
#
# 返回值
# 返回符合条件的新列表。
