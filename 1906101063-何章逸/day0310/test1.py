class Student(object):
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def get__name(self):
        return self.name    #print('姓名:',self.name)
    def get__age(self):
        return self.age#print('年龄:',self.age)
    def get__grades(self):
        return max(self.grades)#print('分数:',max(self.grades))
he=Student('小何',20,[150,150,150])
print('姓名:%s'% he.get__name())
print('年龄:%s'% he.get__age())
print('分数:%s'% he.get__grades())
#he.get__name()
#he.get__age()
#he.grades()
