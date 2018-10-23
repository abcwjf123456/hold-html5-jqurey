def gg(fun):
    def g():
        print('ghh')
        res=fun()
        return res
    return g
@gg
def hhj():
    print('gg')
    return 'ugfvb'

kk=hhj()
print(kk)
