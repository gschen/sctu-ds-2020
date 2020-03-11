#
class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age  = age
        self.score= score
    def get_name(self):
        print("姓名:",self.name)
    def get_age(self):
        print("年龄:",self.age)
    def get_course(self):
        print("最高分:",max(self.score))
x = Student("boboboob","男",[905,80,99])
x.get_name()
x.get_age()
x.get_course()
