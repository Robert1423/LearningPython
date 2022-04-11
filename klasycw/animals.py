class Animal:
    def reply(self):
        self.speak()
    def speak(self):
        print('Animal')

class Mammal(Animal):
    def speak(self):
        print('Mammal')

class Cat(Mammal):
    def speak(self):
        print('Cat')

class Dog(Mammal):
    def speak(self):
        print('Dog')

class Primate(Mammal):
    def speak(self):
        print('Primate')

class Hacker(Primate):
    pass
    #def speak(self):
     #   print('Hacker')

if __name__=='__main__':
    x=Cat()
    x.reply()
    y=Hacker()
    y.reply()