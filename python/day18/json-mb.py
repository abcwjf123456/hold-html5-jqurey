import json
# i=8
# hell0='hgj'
# data=json.dumps(i)
# data1=json.dumps(hell0)#dumps转化成json数据
# f=open('new-file','w')
# f.write(data)

# print(data)
# print(hell0)
# f=open('new-file','r')
# ff=json.loads(f.read())#取出json数据
# print(ff)



# f=open('new-file','r')
# json.dump(data1,f)#等价于f.write(data)，data1=json.dumps(hell0)
# ff=json.load(f)#等价于ff=json.loads(f.read())




with open('new-file','r') as f:
    data=json.loads(f.read())#只要符合json规范就可以用dumps与loads
    print(data)


#pickle不可读计算机可解析

