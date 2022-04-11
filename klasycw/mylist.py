class MyList:
    def __init__(self, start):
        self.wrapped=[]
        for x in start: self.wrapped.append(x)
    def __add__(self, other):
        return MyList(self.wrapped+other)
    def __mul__(self, other):
        return MyList(self.wrapped*other)
    def __getitem__(self, item):
        return self.wrapped[item]
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])
    def append(self, value):
        self.wrapped.append(value)
    def __getattr__(self, item):
        return getattr(self.wrapped,item)
    def __repr__(self):
        return repr(self.wrapped)

class MyListSub(MyList):
    count=0
    def __init__(self, start):
        print('Nowa instancja')
        self.adds=0
        MyList.__init__(self,start)
    def __add__(self, other):
        print('Dodawanie')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__add__(self,other)
    def __mul__(self, other):
        print('Mnozenie')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__mul__(self,other)
    def __getitem__(self, item):
        print('__getitem__',end=' ')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__getitem__(self, item)
    def __len__(self):
        print('Dlugosc')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__len__(self)
    def __getslice__(self, low, high):
        print('Wycinek')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__getslice__(self,low,high)
    def append(self, value):
        print('Append')
        MyListSub.count+=1
        self.adds+=1
        MyList.append(self,value)
    def __getattr__(self, item):
        print('Atrybut')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__getattr__(self,item)
    def __repr__(self):
        print('Repr')
        MyListSub.count+=1
        self.adds+=1
        return MyList.__repr__(self)
    def counts(self):
        print('Liczba wywolan:\n calls: %s, adds: %s' %(MyListSub.count,self.adds))

if __name__=='__main__':
    x=MyList('mielonka')
    print(x)
    print(x[2])
    print(x[1:])
    print(x+['jajka'])
    print(x*3)
    x.append('a')
    x.sort()
    x.reverse()
    for c in x: print(c,end=' ')
    print()
    print('MyListSub:')
    y=MyListSub('mielonka')
    print(y)
    print(y[2])
    print(y[1:])
    print(y+['jajka'])
    print(y*3)
    y.append('a')
    y.sort()
    y.reverse()
    for c in y: print(c)
    print()
    y.counts()
    print()
    z = MyListSub('mielonka')
    print(z)
    print(z[2])
    print(z[1:])
    print(z + ['jajka'])
    print(z * 3)
    z.append('a')
    z.sort()
    z.reverse()
    for c in z: print(c)
    print()
    z.counts()
    print()