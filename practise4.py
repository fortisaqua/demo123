#coding=utf-8
from sys import argv

script, first, second, third=argv
print "The script is called:",script
print "These three varation is :",first+"\n"+second+"\n"+third+"\n"
#用了第2行的这个代码之后，直接在ide上是运行不了这个程序了，只能在命令显示行里打出来
#第4行里有4个变量都赋值了argv，也就是说这4个变量就只能在命令行里打了“python ...”之后
#打上自己定义的4个变量，第一个变量默认为用字符串表示的pyghon程序的名字，也就是在打了“pyuthon”
#之后打的那个名字，是绝对路径也好是相对路径也好，反正就是给你打出来