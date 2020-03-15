class Student(object):
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

wwx=Student('王妍',18,[100,100,100])
print(wwx.get_name())
print(wwx.get_age())
print(wwx.get_course())
