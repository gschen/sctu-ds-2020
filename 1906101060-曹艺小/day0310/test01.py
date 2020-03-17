class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        a = max(self.score)
        return a

bb=Student('Bob',18,[70,80,90])
print(bb.get_name())
print(bb.get_age())
print(bb.get_course())

    
    
            


