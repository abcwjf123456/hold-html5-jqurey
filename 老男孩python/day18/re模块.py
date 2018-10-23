#通配符.
import re
print(re.findall('a..x','aysxf'))

#尖角符^以什么什么开头
print(re.findall('^a..x','accxaccx'))

#$以什么什么结尾
print(re.findall('a..x$','assxassxadjdx'))

#*+?{}重复符号总共四个
#*为紧挨着的元素进行重复，重复次数为无穷次范围(0,无穷次)
print(re.findall('d*','fddffhgfiokndddddddddk'))#['', 'dd', '', '', '', '', '', '', '', '', '', 'ddddddddd', '', '']
# 出现这种结果的原因就是匹配一次重复一次


#+重复次数为无穷次范围(1,无穷次)说明前面必须要有一个字符才能匹配
print(re.findall('alex*','ghhhjjjalexx'))
print(re.findall('alex+','ghhhjjjalexx'))
print(re.findall('alex*','ghhhjjjale'))#['ale']这个可以匹配
print(re.findall('alex+','ghhhjjjale'))#[]这个不能匹配这个就是与他的范围有关这就是*与+的区别
#这种匹配方式叫贪婪匹配?的叫做惰性匹配


#？重复次数为无穷次范围(0，1)
print(re.findall('alex?','ghhhjjjale'))
print(re.findall('alex?','ghhhjjjalexx'))

#{}重复次数范围自己定{0，}==*，{1，}==+，{0,1}==?,{6}==重复6次
print(re.findall('alex{6}','ghhhjjjalexxxxxx'))#一定需要6个x才能匹配成功
print(re.findall('alex{6}','ghhhjjjalexx'))
print(re.findall('alex{0,6}','ghhhjjjalexx'))

#惰性匹配
print(re.findall('alex*?','ghhhjjjalexxxxxx'))#['ale']
print(re.findall('alex+?','ghhhjjjalexxxxxx'))#['alex']

#字符集[]在字符集里面没有特殊符号*啥的都是普通的字符只有三个带有特殊含义的特殊字符
print(re.findall('as[dff]','asdffdff'))#['asd']
print(re.findall('as[df]','asdghasfg'))#['asd', 'asf']就是有或的意思
print(re.findall('as[d*f]','asddghasfg'))#['asd', 'asf']没有特殊符号

#第一种-
print(re.findall('[a-z]','asddghasfg'))#['a', 's', 'd', 'd', 'g', 'h', 'a', 's', 'f', 'g']
print(re.findall('d[a-z]','asddghasfg'))#['dd']只将匹配成功的字符拿出来就停止运行
print(re.findall('d[a-z]*','asddghasfg'))#['ddghasfg']

#第二种^表示非
print(re.findall('q[^a-z]','qgdgqad'))#[]
print(re.findall('q[^a-z]','qadgqad'))#[]
print(re.findall('q[^a-z]','q12345'))#['q1']


#第三种\表示转义我在笔记中有截图(转义时第一步先给python解释器转义然后给re模块所有需要在前面加
# 上r让python解释器不要转义)
print(re.findall('[\d]','1234'))#['1', '2', '3', '4']
print(re.findall('[fg\*]','fg*uj'))#['f', 'g', '*']




#guandaofu |就是这么叫的有或的意思
print(re.findall('df|d','dfdgdd'))#['df', 'd', 'd', 'd']
print(re.findall('df|dg','dgdfdgdf'))#['dg', 'df', 'dg', 'df']


#()能进行分组
print(re.findall('(abc)*','abcabcabc'))#这个有点问题老师没咋说#['abc', '']


#findall与search的区别findall会将字符串变成一个列表然后进行全部的查找而search呢这哥们找到匹配的就
#不会在找下去而且返回的是一个对象，返回不成功就为空
print(re.findall('ab','abfffabggab'))#['ab', 'ab', 'ab']
print(re.search('ab','fffabggab'))#<_sre.SRE_Match object; span=(3, 5), match='ab'>




#正则表达式中，group（）用来提出分组截获的字符串，（）用来分组



print(re.search('ab','fffabggab').group())#ab  group()能将值取出来

# 复制代码
# import re
# a = "123abc456"
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
# print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456

# 1. 正则表达式中的三组括号把匹配结果分成三组
#
#  group() 同group（0）就是匹配正则表达式整体结果
#  group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
# 2. 没有匹配成功的，re.search（）返回None
#
# 3. 当然正则表达式中没有括号，group(1)肯定不对了。



#还有一种group()取值的方式在我的笔记里面有截图具体看截图
print(re.search("(?P<name>[a-z]+)(?P<age>\d+)",'alex12alexw14').group("name"))
print(re.search("(?P<name>[a-z]+)(?P<age>\d+)",'alex12alexw14').group("age"))




