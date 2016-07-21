#coding=utf-8
try:
    filename=raw_input("Put in name of your file >>>")
    writer=open(filename,'w')
    print >> writer,"Stay your blade from the innocent flesh"
    print >> writer,"Hide and play inside"
    print >> writer,"Never compromise the brotherhood"
    print >> writer,"When others are seeking the truth , remember , nothing is true"
    print >> writer,"When others are blindly following the law ane morality , remember , everything is permitted"
    print >> writer,"We walk in the dark , and serve the light"
    print >> writer,"We are assassins"
    writer.close()
    reader=open(filename,'r')
    for eachline in reader:
        print eachline,
    reader.close()
except IOError :
    print 'file open error:'