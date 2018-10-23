# divmod(a,b)函数
# 中文说明：
# divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数
#
# 返回结果类型为tuple
#
# 参数：
# a,b可以为数字（包括复数）
#
# 版本：
# 在python2.3版本之前不允许处理复数，这个大家要注意一下





#题外话list如果添加元素使用insert
# classmates.append('Adam')
# >>> classmates
# ['Michael', 'Bob', 'Tracy', 'Adam']
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
#
# >>> classmates.insert(1, 'Jack')
# >>> classmates
# ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']


#如果删除元素可用pop（）
# 删末尾元素使用pop（）
# > classmates.pop()
# 'Adam'
# >>> classmates
# ['Michael', 'Jack', 'Bob', 'Tracy']
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
#
# >>> classmates.pop(1)
# 'Jack'
# >>> classmates
# ['Michael', 'Bob', 'Tracy']

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
#
# >>> classmates[1] = 'Sarah'
# >>> classmates
# ['Michael', 'Sarah', 'Tracy']
# list里面的元素的数据类型也可以不同，比如：
#
# >>> L = ['Apple', 123, True]



# tuple主要指的是指向永远不变详情查看雪峰老师博客
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819318453af120e8751ea4d2696d8a1ffa5ffdfd7000




# python代码实例：
# >>> divmod(9,2)
# (4, 1)
# >>> divmod(11,3)
# (3, 2)
# >>> divmod(1+2j,1+0.5j)
# ((1+0j), 1.5j)






print(divmod(8,2))#这函数返回的是一个元组