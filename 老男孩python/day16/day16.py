#迭代器和生成器
#迭代器代码
l=[1,2,3,4]
itr_l=l.__iter__() #建立迭代器对象
while True:
    try:
        print(itr_l.__next__())
    except StopIteration:
        print('迭代结束')
        break