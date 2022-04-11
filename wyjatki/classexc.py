class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    #x = General()
    #raise x
    raise General()
def raiser1():
    #x = Specific1()
    #raise x
    raise Specific1()
def raiser2():
    #x = Specific2()
    #raise x
    raise Specific2()

if __name__=='__main__':
    for func in (raiser0, raiser1, raiser2):
        try:
            func()
        except General as X:
            #import sys
            #print('przechwycono:',sys.exc_info()[0])
            print('przechwycono:',X.__class__)