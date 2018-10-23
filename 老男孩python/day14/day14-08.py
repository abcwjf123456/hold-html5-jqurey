p=[
    {'name':'grff','age':122},
    {'name':'grff','age':12},
]
print(list(filter(lambda x:x['age']<=12,p)))
name='gg'
print(bytes(name,encoding='utf-8'))

print(hash(name))
print(list(zip(('a','b','c'),(1,2,3,))))
nr={'gg':14,'dd':13}
print(list(zip(nr.keys(),nr.values())))
# zip只能传列表数组字符串（序列）