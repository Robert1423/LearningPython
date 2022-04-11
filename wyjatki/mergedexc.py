if __name__=='__main__':
    sep = '-'*32+'\n'
    print(sep+'WYJATEK ZGLOSZONY I PRZECHWYCONY')
    try:
        x = 'spam'[99]
    except IndexError:
        print('wykonano except')
    finally:
        print('wykonano finally')
    print('po wykonaniu')
    print(sep+'WYJATEK NIE ZOSTAL ZGLOSZONY')
    try:
        x = 'spam'[3]
    except IndexError:
        print('wykonano excpet')
    finally:
        print('wykonano finally')
    print('po wykonaniu')
    print(sep+'WYJATEK NIE ZOSTAL ZGLOSZONY, WYKONANO ELSE')
    try:
        x = 'spam'[3]
    except IndexError:
        print('wykonano excpt')
    else:
        print('wykonano else')
    finally:
        print('wykonano finally')
    print('po wykonaniu')
    print(sep+'WYJATEK ZGLOSZONY, ALE NIEPRZECHWYCONY')
    try:
        x=1/0
    except IndexError:
        print('wykonano except')
    finally:
        print('wykonano finally')
    print('po wykonaniu')