class Student():
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        print(max(self.course))
a=Student("bob",20,[130,135,125])
a.get_name()
a.get_age()
a.get_course()

