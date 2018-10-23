from functools import reduce
df=[1,3,10]
def foo(fun,arr,init=None):
    if init is None:
        res=arr.pop(0)
    else:
        res=init
    for i in arr:
        res=fun(res,i)
    return res

print(foo(lambda x,y:x*y,df))
# 等价于reduce函数
gh=map(lambda x,y:x*y,df)
print(gh)
print(reduce(lambda x,y:x*y,df))


