#max min
f={'we':100,'df':23,'wu':25}
fe=[
    {'we': 'gg', 'age': 12},
    {'wh': 'gg', 'age': 17},
    {'wj': 'gg', 'age': 18},
]
print(list(max(zip(f.values(),f.keys()))))
# max只能传序列
# 最终玩法
wl=max(fe,key=lambda x:x['age'])
print(wl)