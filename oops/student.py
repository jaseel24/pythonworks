class student:
    name:str
    rollno:int
    course:str
    gender:str
    def __init__(self,name,rollno,course,gender):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.gender=gender

    def print_student(self):
        print(self.name,self.rollno,self.course,self.gender)


s1=student("vinu",5,"bio","male")
s1.print_student()


#course c_id,c_name,c_fee

