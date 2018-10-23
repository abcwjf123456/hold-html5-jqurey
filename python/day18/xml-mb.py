import xml.etree.ElementTree as ET

tree=ET.parse('xml-mb')#解析文本
root=tree.getroot()#获取根节点
# print(root.tag)#打印标签名
# 查
# for i in root:
    # print(i.tag)
    # print(i.attrib)#打印属性名与值
    # print(i.text)#打印值


    # for j in i:
    #     print(j.tag)
# for i in root.iter('gg'):#单独取某个节点
#     print(i.text)

# 修改
# for i in root.iter('gg'):
#     # print(i.text)
#     # newtext=str(i.text+'ggg')#改值
#     # print(newtext)
#     i.set("name2","name6")#改属性值与属性名
#     print(i.attrib)
# tree.write("xml-mb1.xml")#将修改后的值写入文件文件名可以是不相同


#删除
for i in root.findall('com'):#findall这个可以不用双重遍历直接到com节点
    print(i.tag)
    hh=str(i.find('com').text)#有错误还是看笔记吧
    if hh=="gfg":
        root.remove(i)
