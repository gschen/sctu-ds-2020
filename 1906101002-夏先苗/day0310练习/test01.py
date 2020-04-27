class Student(object):
    def __init__(self,name,age,chinses,math,english):
        self.name=name
        self.age=age
        self.chinses=chinses
        self.math=math
        self.english=english
    def get__name(self):
        print(self.name)
    def get__age(self):
        print(self.age)
    def get__score(self):
        print(self.chinses,self.math,self.english)
s=Student('xxm',19,90,89,92)
s.get__name()
s.get__age()
s.get__score()