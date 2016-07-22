import time


class JudgeType(object):
    name = ''
    time = ''

    def get_time(self):
        Stamp = int(time.time())
        timeArray = time.localtime(Stamp)
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print self.time

    def __init__(self):
        self.name = raw_input('put in name of this instance:>>>')

    def type_judge(self, num='asd'):
        print num, 'is:',
        if type(num) == type(0):
            print 'an integer'
        elif type(num) == type(0L):
            print 'a long integer'
        elif type(num) == type(1.1):
            print 'a float'
        elif type(num) == type(0 + 0j):
            print 'a complex number'
        else:
            print 'not a number at all!'


def main():
    tested_num = input('put in a data will be judged:>>>')
    inquester1 = JudgeType()
    inquester1.type_judge(tested_num)
    print 'finished at :',
    inquester1.get_time()
main()
