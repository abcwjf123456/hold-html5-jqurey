# def gg():
#     print('ygy')
#     def gg():
#         pass
# 函数嵌套就是在函数里面在定义一个函数
def father(name):
    print('你的名字 %s' %name)
    def son():
        print('son')
    son()
    print(locals())
father('hh')
# 函数及变量,闭包封装了变量上例子就是闭包