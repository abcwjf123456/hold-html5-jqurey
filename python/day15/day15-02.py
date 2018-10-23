# with open('df.txt','r') as d:
#
#     d.seek(10)
#     print(d.tell())

# with open('df.txt','rb') as d:
#     d.seek(10,1)
#     print(d.tell())

with open('df.txt','rb') as d:
    d.seek(-3,2)#倒着seek
    print(d.tell())
    print(d.read())
# read()代表读取的是字符，其他都是以字节为单位如seek,tell,truncate