# coding=utf-8
class Practise12(object):
    version = 1.1
    owner = ''

    def showname(self):
        print 'name of this object is:>>>', self.name
        print 'name of this object\'s class is:>>>', self.__class__.__name__
        print 'super name of this object is:>>', self.supername

    def fun1(self, x=0, y=100):
        if(x >= 23)and\
                (y <= 34):
            print 'valid!'
        elif(x <= 0)and\
                (y >= 100):
            print 'not so valid!'
        else:
            print 'invalid!'

    def __init__(self, name='dismond'):
        self.name = name
        sname = raw_input("put in a supername>>>")
        self.supername = sname
        # print 'an instance of %s has been made by
        # %s'%(self.__class__.__name__,name)

instance1 = Practise12("helloworld")
instance1.fun1()
instance1.fun1(23, 34)
print '\n' * 3, '-' * 60
instance1.showname()

# 这里用到的一个新东西就是换行继续，在上面的if语句里就可以看到判定分行了
# 但是在分行的时候要在右边放上一个"\"符号来声明换行！


def swap(x, y):
    x, y = y, x
    return x, y
ins1 = Practise12()
ins2 = Practise12()
ins1.showname()
ins2.showname()
print '\n' * 3
ins1, ins2 = swap(ins1, ins2)
ins1.showname()
ins2.showname()

a = 123
b = 456
a, b = swap(a, b)
print 'a=%d' % a
print 'b=%d\n\n' % b
# python的函数可以返回多个值，只要用逗号隔开就可以了，所以在函数上
# 就只有传值，如果想通过函数改变某一个或多个对象的话，那就用返回的方式
# 就好像上面的 swap 函数一样，交换两个对象的内容，就可以在函数里先处理
# 交换，再用返回的形式重新装回两个对象对应的标签，这样就完成了互换
# 以往写C和C++的时候只能返回一个值，所以需要通过函数引用来改变引用
# 变量的值，python里就没这么复杂了，直接返回就好了,对于声明的单个变量
# 也是，用这个swap函数的返回值来实现互换，而不是引用过去直接对两个变量改写
ins1, ins2 = swap(ins1, ins2)
print cmp(ins1, ins2)
print repr(ins1)
print str(ins2)
print type(ins1)
print isinstance(ins1, Practise12)

# 对于一个对象来说，repr和str函数都类似于输出一句“。。。类型的在一个具体内存地址的对象”
# 这样的话，至于对象的比大小。。。。可能就是地址上的大小，跟设置的内容无关了

print '\n' * 3
clist = [ins1, ins2, instance1, 'hello', 123, 123.45, 34 + 23j]
print clist[0:2]
# 只要是定义好的对象，也是可以放进列表里的
