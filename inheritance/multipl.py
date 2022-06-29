class P1():
    def m1(self):
        print("car")
class P2:
    def m2(self):
        print("bike")
class P3(P1,P2):
    def m3(self):
        print("lorry")

ppd=P3()
ppd.m1()
ppd.m2()
ppd.m3()
