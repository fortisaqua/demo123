#coding=utf-8
x="There are %d types of people" % 10
binary="binary"
do_not="don't"
y="Those who know %s and those who %s" % (binary,do_not)

print x
print y

print "I said : %r" % x
print "I also said : %r" % y

hilarious=False
joke_evaluation="Isn't that joke so funny? \n %r"
print joke_evaluation % hilarious

w="This is the left side of..."
e="a string with a right side."
print w+e
print w,e
# 以往使用的转义字符在python里也通用，在python里，字符串里带 % 的变量可以在
# 字符串定义的时候设置，就好像一般的输出一样，也可以先放着，比如上面的joke_evaluation
# 一开始就没有对那个 % 进行解释，而是在输出的时候再具体到了哪个变量
#以上两种对w和e的输出中，不同在于，用w+e输出，两个字符串就直接连着输出了，但是用w,e输出，两个字符串之间会添加一个空格符号

#最上面一行的“coding=utf-8”必须要加，否则就算是注释，只要出现中文就不通过编译！