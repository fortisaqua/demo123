# coding=utf-8
alist=[1,2,"hello world!",4]
print alist
print alist[0]
print alist[2:]
print alist[:3]
alist[2]="sdfsfwrfarf"
print alist[2:3]
#对于这样的切片访问，一般都是大于等于左边的序号，小于右边的序号，并且
#序号也是从0开始算的,python里的数组和元组最爽的一点就是一组之内的内容
#也可以完全不一样

print "\n\n\n"
print "-"*30

atuple=('robots',123,43,'try')
print atuple
print atuple[:3]

blist=[213,424312,2345,2342,31243,124,51312,236,234]
for i in range(len(blist)):
    if blist[i]>=2345:
        print blist[i], '(%d)' % i
print '\n'*3
clist=['when','others','are','blindly','following','the','law','and','morality',
       'remember','everything','is','permitted']
for i,word in enumerate(clist):
    print word,'(%d)'%i

dlist=[a**2 for a in range(4)]
for j,number in enumerate(dlist):
    print number,'(%d)'%j

print '\n'*3+'-'*40

elist=[b**3 for b in range(16) if not b%2]
for k,data in enumerate(elist):
    print data,'(%d)'%b,'(%d)'%k

#如果要在定义数组的时候就在数组里处理东西，那么注意，在数组生成之后
#数组生成时所用的临时变量，在这个for循环里有效，但是一个就是一个，它并没有保存
#到每一个对应的有效数组元素中去，比如上面的变量b，在经过了0到15的16次循环之后
#b就跟着成了15，因为这里的b，也就是以前for循环里的一个临时变量，但是这里不同的是
#在生成数组的时候即使用for循环，一般不会去关心这些临时变量有啥意义
#python的这个用法有点像do while 用法，不过自由度高了超级多。。。。。。还能在写了for
#之后随即跟上一个判定条件。。。。。没有括号的对应还真是不适应。。。。。。。