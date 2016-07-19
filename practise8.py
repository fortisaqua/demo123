#coding=utf-8
alist=['name1','name2']
blist=['land','ocaen']
adic={'host':alist}
adic['earth']=blist
print adic
print adic.keys()
print adic['host']
print adic['earth']
for key in adic:
    print key,adic[key]
    print key
    print adic,"\n"
print adic
#python中的for循环也太简单了。。。。自动迭代，只要注意的是写完了for的一行之后要打上一个双引号
#并且没有了用C所用的for循环里的大括号对应，只要 缩进上对应就是一组了。。。。。。后面的if，while
#语句，也都是在写了if，while对应的判定之后打上一个双引号，下面的条件语句也全是靠缩进来打包