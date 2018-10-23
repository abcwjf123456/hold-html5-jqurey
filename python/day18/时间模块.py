import time
# 有转换截图在笔记里面
# 时间戳
print(time.time())#1530756050.612231这时间代表1970到现在用了多少秒
# 结构化时间
# print(time.localtime())#当地时间
t=time.localtime()
print(t.tm_year)
print(time.gmtime())#世界标准时间
# 结构化时间转换成时间戳
print(time.mktime(time.localtime()))
# 将结构化时间转换成字符串时间
print(time.strftime('%Y.%m.%d %X',time.localtime()))
# 将字符串时间转换成结构化时间
print(time.strptime('2018:7:3:10:34:20','%Y:%m:%d:%X'))




# 不想排就用这


print(time.asctime())#参数结构化参数
print(time.ctime())#参数为时间戳


import datetime
print(datetime.datetime.now())