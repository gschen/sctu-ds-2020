class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_score(self):
       print( max(self.score))
h=Student  ("lisa",19,[100,99,98])
h.get_name()
h.get_age()
h.get_score()
 