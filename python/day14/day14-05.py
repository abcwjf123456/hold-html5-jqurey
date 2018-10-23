num=[1,2,3,4]
def foo(fun,arr):
    ret=[]
    for i in arr:
        res=fun(i)
        ret.append(res)
    return ret

var=foo(lambda x:x+2,num)
print(var)
# 等价于map()
print(list(map(lambda x:x+1,num)))
