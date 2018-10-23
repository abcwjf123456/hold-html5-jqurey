# 迭代器与生成器
# 对比例子
# def scz():
#     ret=[]
#     for biaoz in range(100):
#         ret.append('包子%s' %biaoz)
#     return ret
# def xfz(res):
#     for index,hh in enumerate(res):
#         print('第几%s人,吃了包子%s' %(index,hh))
# res=scz()
# xfz(res)
# 生成器写法
def fg():
    print('hh')
    yield 1
    print('gg')
    k=yield 2
g=fg()
print(g.__next__())
g.send(2)

# yield后面的值为return值send传的值是给yield然后传给k