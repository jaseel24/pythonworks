class course:
    c_id=int
    c_name=str
    c_fee=int
    c_duration=str
    def __init__(self,**kwargs):
        self.c_id=kwargs.get("c_id")
        self.c_name=kwargs.get("c_name")
        self.c_fee=kwargs.get("c_fee")
        self.c_duration=kwargs.get("c_duration")
    def print_course(self):
        print(self.c_id,self.c_name,self.c_fee,self.c_duration)


crs=course(c_id=3245,c_name="physics",c_fee=17000,c_duration="2year")
crs.print_course()