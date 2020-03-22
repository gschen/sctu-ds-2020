 class Student():
     def __init__(self,name,age,score):
         self.name=name
         self.age=age
         self.score=score
     def get_name(self):
         print(self.name)
     def get_age(self):
         print(self.age)
     def get_course(self):
         print(max(self.score))
 m=Student("x",20,[98,95,100])
 m.get_name()
  m.get_age()
m.get_course()