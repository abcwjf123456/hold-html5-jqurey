# with open('gg','w+') as d:
#     print(d.read())
#     print(d.writable())
#     # d.write('ft')
#     # d.writelines(['tygty','hughy'])
#     d.write('ft')
# #     b模式不能指定编码
# 字符串- encode》字节
# 字节-decode》字符串
# with open('gg','rb') as h:
#     print(h.read().decode('utf-8'))

# x='ed'
# l=x.encode('utf-8')
# l=bytes(x,encoding='utf-8')
with open('gg','wb') as h:
    print(h.write(l))
    # 刷新
    h.flush()
#     截取会删除没有截取的部分而且不能用w+
h.truncate(10)

