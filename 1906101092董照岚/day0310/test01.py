class Student():
    def __init__ (self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print("姓名",self.name)
    def get_age(self):
        print("年龄",self.age)
    def get_score(self):
        print("成绩",self.score)

a=Student("Lisa",19,70)
a.get_score()
a.get_age()
a.get_name()
