#coding=utf-8
def addself(x):
    'apply + operation to argument'
    return (x+x)
print addself(12)
print addself('inquestion')
#函数的定义和调用方法和其他语言差不多，这里有一行‘apply。。。。’其实也是注释
#不是非要在前面添加上井号才行的

print '\n'*3+'-'*50+'\n'*3
def func(default=True):
    if default:
        print 'in default mode'
    elif default==False:
        print 'not in default node'
    print 'done'
func()
func(False)

#在func函数中，其参数里就有一个赋值的操作，但是这不是说任何输入都会规格化
#而是说对于这个函数的default字段，可以不输入，运行时就按照函数设定的这个
#“默认值”来运行