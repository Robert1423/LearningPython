class Scene:
    def action(self):
        self.customer=Customer()
        self.clerk=Clerk()
        self.parrot=Parrot()
        self.customer.line()
        self.clerk.line()
        self.parrot.line()
class Line:
    def line(self):
        print(self.__class__.__name__+': ',repr(self.text()))
class Customer(Line):
    def text(self):
        return "To juz ekspapuga!"
class Clerk(Line):
    def text(self):
        return "nie, wcale nie..."
class Parrot(Line):
    def text(self):
        return None

if __name__=='__main__':
    S=Scene()
    S.action()