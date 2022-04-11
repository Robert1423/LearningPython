class Adder:
    def __init__(self,value):
        self.data=value
    def add(self,x,y):
        print('Nie zdefiniowano')

class ListAdder(Adder):
    def __init__(self):
        Adder.__init__(self,[])
    def add(self,x,y):
        if isinstance(x,list) & isinstance(y,list):
            for i in y:
                x.append(i)
            self.data=x
        else:
            Adder.add(self,x,y)
    def __add__(self, other):
        if isinstance(other,list):
            self.add(self.data,other)
        else:
            Adder.add(self,self.data,other)

class DictAdder(Adder):
    def __init__(self):
        Adder.__init__(self,{})
    def add(self,x,y):
        if isinstance(x,dict) & isinstance(y,dict):
            res={}
            res.update(x)
            res.update(y)
            self.data=res
        else:
            Adder.add(self,x,y)
    def __add__(self, other):
        if isinstance(other,dict):
            self.add(self.data,other)
        else:
            Adder.add(self,self.data,other)