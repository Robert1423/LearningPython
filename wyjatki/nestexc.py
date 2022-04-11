def action2():
    print(1+[])

def action1():
    try:
        action2()
    except TypeError:
        print('wewnetrzne try')

if __name__=='__main__':
    try:
        action1()
    except TypeError:
        print('zewnetrzne try')