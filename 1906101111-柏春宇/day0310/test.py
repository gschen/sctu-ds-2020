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
        print(max(self.score))


a=Student('柏春宇',18,[107,118,124])
a.get_name()
a.get_age()
a.get_score()