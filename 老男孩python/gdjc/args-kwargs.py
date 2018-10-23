def greet_me(**kwargs):
    for key, value in kwargs.items():#Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
        print("{0} == {1}".format(key, value))#相当于%的使用


greet_me(name="yasoob")
# name == yasoob