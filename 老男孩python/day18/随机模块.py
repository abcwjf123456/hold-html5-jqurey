import random
# print(random.random()*10+10)
# print(random.randint(1,3))#可以取到3取值都是整型
# print(random.randrange(1,3))#这个不可以取值到3
# print(random.choice([1,5,6,7,8]))#可以随机出现一个
# print(random.sample([1,3,5,6,7],2))#可以随机出现自己定义的个数
# print(random.uniform(1,3))#任意区间浮点型
# ret=[1,3,4,5]
# random.shuffle(ret)
# print(ret)
# # shuffle用来打乱列表



def gg():
    rtt = ''
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        f=str(random.choice([num,alf]))
        rtt=rtt+f
    return rtt
print(gg())