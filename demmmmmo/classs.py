class Car:
    color:str
    fuel:str
    tankcapacity:int
    def __init__(self,color,fuel,tankcapacity):
        self.color=color
        self.fuel=fuel
        self.tankcapacity=tankcapacity
    def print_featurs(self):
        print(self.color)

featr=Car("black","diseal",40)
featr.print_featurs()

