#课堂检测题


class Student():
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
        
xiaom=Student('小明','18岁',[66,88,98])
print(xiaom.get_name())
print(xiaom.get_age())
print(xiaom.get_course())

