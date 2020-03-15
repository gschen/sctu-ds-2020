class Student():
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_coures(self):
        return max(self,_scores)
lzh=Student('张三',15,[90,89,99])
print('name': %s' %(lzh.get_name()))
print('age: %s' %(lzh.get_age()))
print('score: %s' %(lzh.get_course()))

