#课堂检测

class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        print(max(self.score))
m=Student("黄柏林",19,[99,99,99])
m.get_name()
m.get_age()
m.get_course()