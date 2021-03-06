# 功能：
# 函数的作用是将一个数字或base类型的字符串转换成整数。
#
#
#
# 函数原型：
# int(x=0)
#
# int(x, base=10)，base缺省值为10，也就是说不指定base的值时，函数将x按十进制处理。

# 注意：
# 1. x 可以是数字或字符串，但是base被赋值后 x 只能是字符串
#
# 2. x 作为字符串时必须是 base 类型，也就是说 x 变成数字时必须能用 base 进制表示


print(int(3.14) )           # 3
print(int(2e2))           # 200
# print(int(10, 8))         # 出错，base 被赋值后函数只接收字符串 #后面的base值也就是例如8进制10等于8，100等于64及8的两倍
print(int('FZ', 36))
print(int('0x10', 36))
#表示36进制转换不懂




# 2. x 是字符串的情况：
# int('23', 16)      # 35
# int('Pythontab', 8)      # 出错，Pythontab不是个8进制数
#
#
# 3. base 可取值范围是 2~36，囊括了所有的英文字母(不区分大小写)，十六进制中F表示15，那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35
# int('FZ', 16)      # 出错，FZ不能用十六进制表示
# int('FZ', 36)      # 575




# 3. 字符串 0x 可以出现在十六进制中，视作十六进制的符号，同理 0b 可以出现在二进制中，除此之外视作数字 0 和字母 x
# int('0x10', 16)  # 16，0x是十六进制的符号
# int('0x10', 17)  # 出错，'0x10'中的 x 被视作英文字母 x
# int('0x10', 36)  # 42804，36进制包含字母 x