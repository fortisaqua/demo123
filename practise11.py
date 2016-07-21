#coding=utf-8
class FirstClass(object):
    """my first class"""
    version=1.0
    owner='ezio'
    def __init__(self,nm='desmond'):
        #构造这个类的一个对象的函数，这个__init__的函数名是固定的
        self.name=nm
        print 'an instance of class FirstClass is created for',nm
    def showname(self):
        #输出当前对象的对象名
        print 'This instance\'s name is',self.name
        print 'This instance\'s class name is',self.__class__.__name__
    def showver(self):
        #输出当前对象所属类的基本属性值
        print self.owner,'\n',self.version
    def addme(self,x):
        return x*2

firstclass_object=FirstClass('sucker')
firstclass_object.showname()
firstclass_object.showver()

print '\n'*3,'-'*50,'\n'*3

print dir(firstclass_object)
print '\n',type(firstclass_object)
#上面的类的定义中并没有name这个字段，但是在创建函数里就有这个，
#因为在python里，如果想在创建对象的时候添加属性字段是可以的，这里的
#name就是一个例子，它在改写的创建函数__init__里就写了self.name，那么在执行
#完了__init__函数之后，这个实例就会比它所属的类要多出一个name字段，注意
#这个name字段在原来的类里确实是没有的。。。。还能这么玩