class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print("name:%s,age:%d,sex:%s"%(self.name,self.age,self.sex))
class Teacher(Person):
    def __init__(self,name,age,sex,collage,professional):
        Person.__init__(self,name,age,sex)
        self.collage=collage
        self.professional=professional
    def personInfo(self):
        super().personInfo()
        print("collage",self.collage)
        print("professional",self.professional)
    def teachobj(self):
        print("今天讲了：面向对象设计程序")
a=Teacher("Bob",28,"男","会计学","会计")
a.personInfo()
a.teachobj()