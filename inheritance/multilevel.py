class P1():
    def m1(self):
        print("car")
class P2(P1):
    def m2(self):
        print("bike")
class P3(P2):
    def m3(self):
        print("lorry")
pd=P2()
pd.m1()
pdd=P3()
pdd.m2()

