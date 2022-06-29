class Parent:
    def properties(self):
        props={"mobile":"iphone","bike":"passion pro"}
        return props
class Child(Parent):
    def properties(self):
        props=super().properties()
        props={"car":"swift"}
        return self.props
childerns=Child()
print(childerns.properties())
