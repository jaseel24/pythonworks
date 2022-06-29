class Parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passinon pro")
class Child(Parent):
    def phone(self):
        print("iphone")
    def bike(self):
        print("duke")


children=Child()
children.phone()