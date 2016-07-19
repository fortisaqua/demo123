#coding=utf-8
prompt='> '
print "put in the first varation: ",
first=raw_input(prompt)
print "put in th second varation: ",
second=raw_input(prompt)

print "the varations you just put in is :\n",first+"\n"+second
print "%s\n%r" % (first,first)
#print "%d\n" % first
#这里的row_input()输入的全部都是字符串，所以运行上面那行就会出错
#在第一行就加了 coding=utf-8 之后，输入中文也是可以的，只不过
#中文用 %r 输出的话，会转变成中文标准对应的英文码
print "\n\n\n"
third=raw_input("put in the third varation: "+prompt)
print "the third varation is:\n%r" % third
#也就是说对于输入想要说明的话，不用单独输出说明了再打输入函数，只要在
#raw_input()函数的括号里面直接写双引号括起来的字符串就可以了，这里的
#third就是用了这个方法，但是注意，如果想组合几个字符串在input函数里，
#要用 + 来把这些字符串组合成一个