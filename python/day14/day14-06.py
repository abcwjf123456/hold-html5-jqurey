
fg=['df','df-sb','gt-sb']

def endsw(n):
    return n.endswith('sb')
def dg(fun,sd):
    gh=[]
    for i in sd:
        if not fun(i):
            gh.append(i)
    return gh

hh=dg(endsw,fg)
print(hh)
# 等价于filter
print(list(filter(lambda x:not x.endswith('sb'),fg)))