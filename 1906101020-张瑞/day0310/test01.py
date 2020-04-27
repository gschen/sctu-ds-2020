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

xs=Student('雪松',20,[93,95,90])
xs.get_name()
xs.get_age()
xs.get_score()
