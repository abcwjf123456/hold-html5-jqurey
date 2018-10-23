def gg(fun):
    def g(*args,**kwargs):
        print('ghh')
        res=fun(*args,**kwargs)
        return res
    return g
@gg
def hhj(name,age):
    print('gg')
    print(name)
    return 'ugfvb'

kk=hhj(11,'hg')
print(kk)
