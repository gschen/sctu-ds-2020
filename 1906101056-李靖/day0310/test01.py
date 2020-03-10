class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_name(self):
        if isinstance(self.name,str):
            return self.name

    def get_age(self):
        if isinstance(self.age,int):
            return self.age
    def get_course(self):
        a=max(self.score)
        if isinstance(a,int):
            return a

she=Student('limuzi',18,[77,88.99])
print(she.get_name())
print(she.get_age())
print(she.get_course())
       