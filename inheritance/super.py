class Parent:
    def props(self):
        self.props={"mobile":"nokia","bike":"pulser"}
        return self.props
class Child(Parent):
    def props(self):
        props=super().props()
        props["car"]="swift"
        return props
chh=Child()
print(chh.props())
