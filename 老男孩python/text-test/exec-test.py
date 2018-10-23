# exec 函数功能：执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。

# 注意： 在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python 2中有一个 execfile() 函数。可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了。
#
# 所以类似功能的函数在python2中是execfile。
# exec(object[, globals[, locals]])
#
#
#
# 参数
# object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，该字符串会先被解析为一组Python语句，然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
#
# globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
#
# locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。
#
# 返回值
#
# exec 返回值永远为 None。


exec ('print("hbhh")')
def gg():
    print('hhh')
exec('gg()')
# 多行语句字符串
exec ("""for i in range(5):
       print ("iter time: %d" % i)
   """)
exec("""for j in range(3): print('time is: %d' % j)""")