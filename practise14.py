#coding=utf-8
from numpy import *
string1='abcdefghijklmn'
print string1[::-1]
print '\n'*2,'-'*65
print string1[::-2]
print '\n'*2,'-'*65
print string1[::1]
print '\n'*2,'-'*65
print string1[::3]

list1=[232,'sdfas',134.2132,'dafea']
print list1[::-1]
print '\n'*2,'-'*65

temp_str=string1[0:3]
temp_str+=(string1[9:len(string1)])
print temp_str
print string1[9:len(string1)]
print string1[4:5]
print '\n'*2,'-'*65

blist=[1,2,3,4,5,6,7,8,9,10]
templist=blist[0:3]
templist+=blist[6:9]
print templist
print '\n'*2,'-'*65
#要是想合并多个数组，还是直接用加法吧。。。。还简单直接点，什么多维切片
#以及append函数，先不考虑了，数组之间的相加而不是添加元素，就用相加。。。。。。。

templist1=[1,2,3,7,8,9]
print templist is templist1
tl1=[1,2,3,7,8,9]
print templist1 is tl1
tl2=tl1
print tl1 is tl2
x=12345.123
y=12345.123
print x is not y
print not (x is y)
print id(x),'\n',id(y)
print 'id of templist is:',id(templist)
print 'id of templist1 is:',id(templist1)
print 'id of tl1 is:',id(tl1)
print 'id of tl2 is:',id(tl2)

#从上面的结果也可以看出，对于简单的单个数据对象，就是相等即同一个，内存地址都是一样的
#但是对于比单个数据复杂的数据对象，比如这里的一个列表（可以存放不同类型数据的数组），
#那么相同的列表就不一定是同一个了，这里的templsit1和tl1就是很好的
#布尔值的最后两个输出也可以看到，not关键字可以当做英语语法的not一样写 is not
#也可以看成是非判断一样写 not (。。。is。。。) 这样的形式