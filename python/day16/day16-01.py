#迭代器的好处使用卖包子例子
def gg():
    for i in range(10):
        yield 'gtf %d' %i
w=gg()
g=w.__next__()
print(g)
k=w.__next__()
print(k)
