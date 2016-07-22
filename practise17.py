# coding=utf-8
import random
import string
print random.randrange(2, 2000)
print random.uniform(2, 2008)
# randrange功能返回的是随即整数，uniform返回的是随机浮点数
for i in range(1, 100, 4):
    print random.uniform(i, i + 4)
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print alist[::-3]
# 对于[::]这样的切片操作，一定是步进切片的，而第三个“步长”的
# 参数有正负之分，正的就是序号从左往右，负的就是从右往左，去了
# 符号之后的数字就是步长

print len(alist)
for j in range(-1, -15, -1):
    print alist[:j], "[%d]" % j
# 在切片的[:]中，右边一个数字如果是负数，它代表的就是从右往左扣掉
# 这个负数对应的绝对值个数字，比如这里有alist[:-3],那么就是切出了
# 从0号到len（alist）-3号，而这里的步进写了个-1，目的是保证负数的
# 顺序输出，因为在range（a,b）里，它读入的范围永远是从a到b，那么
# 一旦a小于b了，整个循环就根本不会输出了

print string.octdigits
print string.hexdigits
