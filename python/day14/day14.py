# 作用域

def gg():
    print('gg1')
def gg1():
    print('gg2')
    return gg
res=gg1()
print(res())
# gg为内存地址