class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_name_and_age(self):
        print(self.name,self.age)
    def get_course(self):
        print(max(self.score))

xiaom=Student('xiaom',19,[100,120,110])
xiaom.get_name_and_age()
xiaom.get_course()