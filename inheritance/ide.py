class Editor:
    def functionalites(self):
        self.fun=["execute","save"]
        return self.fun
class Funs(Editor):
    def functionalites(self):
        add=super().fun
        add.append("debug")
cch=Funs()