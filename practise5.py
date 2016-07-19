#coding=utf-8
filename=raw_input("get a file name:>>>")
txt=open(filename)
print "your file name is :%s\n" % filename
print txt.read()

#就算是只要写一个文件名，但是也要注意路径和格式，这里的文件就在当前python程序所在目录，所以
#可以直接写，但是格式txt的后缀还是要加的