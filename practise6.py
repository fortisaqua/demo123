filename=raw_input("put in the file name :>>> ")
print "we are going to erase %r." % filename
print "If you don't want that , hit CTRL-C (^C)"
print "If you do want that , hit RETURN."

raw_input(">>> ")

print "Opening the file"
target=open(filename,'w')

print  "Truncating the file.   Goodbye!"
target.truncate()

print >> target,'hello world , this is %s\n' % filename
text=open(filename,'r')
print text.read()