class Parent:
    def phone(self):
        print("nokia")
    def car(self):
        print("ritz")
class Child(Parent):
    pass
ch=Child()
ch.phone()
ch.car()