class MyError(Exception): pass
def stuff(file):
    raise MyError()
if __name__=='__main__':
    file = open('data','w')
    try:
        stuff(file)
    finally:
        file.close()
    print('nie doszlismy tutaj')