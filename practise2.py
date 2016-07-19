#coding=utf-8
print "Mary has a lttle lamb."
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary went."
print "."*10

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12

formatter="%r %r %r"
print formatter
#print formatter % (formatter,formatter)
print formatter % (formatter,formatter,formatter)
#如果把上面注释里的那句话放出来，一样可以运行，从25行开始之后的程序就不运行了，
#并且会在运行的一开始告诉你第25行有错误

print "\n\n\n"

days="Mon Tue Wed Thu Fri Sat Sun"
months="Jan\nFeb\nMar\nApr\nMay"

print "Here are the days : \n",days
print "Here are the months : \n",months
print "These months : \n%r" % months
longstring='''
134151351351
134151
jdsiognrignwerg
wionriowurjwgiorh
'''

longstring1="""
134151351351
134151
jdsiognrignwerg
wionriowurjwgiorh
"""

print "%r\n%r" % (longstring,longstring1)
print longstring
print longstring1
#用%r输出的内容里不会去格式化处理，如果是字符串，甚至还会输出单引号
#来表示“这是字符串”
#另外，在用 %r 输出用三个引号括起来的长文本时，输入的时候按的回车会
#显示出来，并且不会换行输出，不管是三个引号是单是双，如果直接输出
#那么换行会有效，并且整体的上下在输出的时候会多出两个换行
