#coding=utf-8
from __future__ import division
import math
import cmath
from decimal import Decimal

print 1/4
#从__future__包里引入division之后，整数的处罚也能被
#看成是真正的除法，这样也能输出浮点数的结果
print 1//4
#地板除就是这里的两个斜杠组成的运算符，功能就是不管什么
#除法直接舍去小数部分，但是这是向下取整，所以如果是负数
#比如结果是-1.3，那么结果会是-2
print coerce(123L,1+3J)
#coerce函数也就是一个“带着变复杂”的函数，简单的数字类型
#被复杂的数字类型同化，这里的长整型数字就成了复数
print round(3.123454523,8)
print round(-3.3)
print round(-0.7)
print math.floor(-3.3)
print math.floor(-0.7)
#round函数也就是取有效数字的四舍五入的操作，这里后面的一个数字就是
#保留的位数，上面就是保留小数点后8位，如果不写，默认为0，即保留整数
#的四舍五入对于round和floor，它们都是保留有效数字，但是floor操作一
#定是向下取整而对于round，除了绝对值小于1的，都是真的在做取有效数
#字，当绝对值小于1时，用round取整也是得到-1的

#print 'a'+3
print chr(ord('a')+3)
#在python里，没有字符类char，所以一个字符不能通过加减数字来直接变字符
#需要用ord函数来转换成ascii编码对应的数字，加减数字之后再用chr函数把
#计算后的数字转换回ascii编码对应的字符

dec1=Decimal('23.343')
print dec1
print dec1

