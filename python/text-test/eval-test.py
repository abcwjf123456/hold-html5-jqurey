# 函数定义：
# eval(expression, globals=None, locals=None)
#
# 将字符串str当成有效的表达式来求值并返回计算结果。globals和locals参数是可选的，如果提供了globals参数，那么它必须是dictionary类型；如果提供了locals参数，那么它可以是任意的map对象。
#
# python的全局名字空间存储在一个叫globals()的dict对象中；局部名字空间存储在一个叫locals()的dict对象中。我们可以用print (locals())来查看该函数体内的所有变量名和变量值。
#
# eval()主要作用：
# 1）在编译语言里要动态地产生代码，基本上是不可能的，但动态语言是可以，意味着软件已经部署到服务器上了，但只要作很少的更改，只好直接修改这部分的代码，就可立即实现变化，不用整个软件重新加载。
#
# 2）在machin learning里根据用户使用这个软件频率，以及方式，可动态地修改代码，适应用户的变化。
#
#
# 安全问题：
# 因为eval的特型， 很可能被黑客利用，造成安全问题。
#
# 怎么避免安全问题？
#
# １、自行写检查函数；
#
# ２、使用ast.literal_eval代替


#ast.literal_eval他会检查python数据类型的安全性我查看百度就这么一点区别。







# eval与exec的差别可参照这并不完全正确可看具体文档
num1=1
num2=2
num3=exec('num1+num2')
num4=eval('num1+num2')
print(num3)
print(num4)

x = 1
y = 1
num1 = eval("x+y")
print(num1)


def g():
    x = 2
    y = 2
    num3 = eval("x+y")
    print(num3)
    num2 = eval("x+y", globals())
    # num2 = eval("x+y",globals(),locals())
    print(num2)
    # num1的值是2；num3的值也很好理解，是4；num2的值呢？由于提供了globals()
    # 参数，那么首先应当找全局的x和y值，也就是都为1，那么显而易见，num2的值也是2。如果注释掉该句，
    # 执行下面一句呢？根据第3)点可知，结果为4

    g()

