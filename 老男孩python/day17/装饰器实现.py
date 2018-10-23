# def gg(hh):
#     def gg():
#         pass
#     return hh
# # 装饰器
def gg(hh):
    def g():
        print('ggg')
        hh()
    return g
# 装饰器框架
@gg#要装饰谁就放在谁前面相当于hhj=gg(hhj)
def hhj():
    print('rr')
hhj()
# tr=gg(hhj)#返回gg函数地址
# tr()#执行的是g函数
# 装饰器使用


# hhj=gg(hhj)=@gg
# hhj()