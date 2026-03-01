class Student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade

    def display(self):
        print(f"Student id: {self.id} Name:{self.name} Grade: {self.grade}")


s1=Student(12,"Dev","A")
s2=Student(13,"Raj","B")
s3=Student(14,"Krishna","A")
s1.display()
s2.display()
s3.display()