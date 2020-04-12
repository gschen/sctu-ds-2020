# 定义一个学生Study类
class Student():
    def _init_(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_score(self):
        print(self.score)
a=Student('小明',18,95)
a.get_name
a.get_age
a.get_score