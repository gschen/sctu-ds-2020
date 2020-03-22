class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.score)
xm=Student('大熊',18,[6,20,17])
print(xm.get_name())
print(xm.get_age())
print(xm.get_score())