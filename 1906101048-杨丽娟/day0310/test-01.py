class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_score(self):
        print(self.score)
a=Student('y',18,[121,112,111])
a.name=name
a.age=age
a.score=score