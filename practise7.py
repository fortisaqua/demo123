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