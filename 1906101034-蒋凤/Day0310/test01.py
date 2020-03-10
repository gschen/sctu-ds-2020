class Student(object):
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)

pa=Student('博一',15,[90,88,99])
print('name:%s'%(pa.get_name()))
print('age:%s'%(pa.get_age()))
print('最高分:%s'%(pa.get_course()))