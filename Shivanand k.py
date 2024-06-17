stud={}
class Student:
    def __init__(self, name, regno, m1, m2, m3):
        self.name = name
        self.reg_no = reg_no
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
num=int(input("how many students you need to craete :"))
for i in range(num):
        name=input("enter a student name :")
        regno=int(input("eneter student reg no :"))
        m1=int(input("enter student M1 : "))
        m2=int(input("enter student M2 : "))
        m3=int(input("enter student M3 : "))
        st=student(name,regno,m1,m2,m3)
        stud[regno]=st
def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3
average_marks = calculate_average(m1, m2, m3)
print("Average Marks:", average_marks)











        

