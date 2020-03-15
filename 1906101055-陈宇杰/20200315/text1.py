class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def peronInfo(self):
        print(self.name,self.age,self.sex)

xiaoM=Person('王小明',20,'男')
xaioM.peronInfo()

class Teacher(Person):
    def __init__(sef,name,age,sex,collage,professional):
        self.name=name
        self.age=age
        self.sex=sex
        self.collage=collage
        self.professional=professional

    def peronInfo(self):
        print(self.name,self.age,self.sex,self.collage,self.professional)
    def teachonj(self):
        return '今天讲了：面向对象'
laoc=Teacher('程老师',20,'男','信工','信息管理')
laoc.peronInfo()

class Student(Persin):
    def __init__(self,name,age,sex,collage,classNub):
        super().__init__(name,age,sex)
        self.collage=collage
        self.classNub=classNub

    def peronInfo(self):
        print(self.name,self.age,self.sex,self.collage,self.classNub)

    def study(self,object):
        recept=object.teachobj()
        print('老师{},我学会了'.format(recept))

laog=Student('张三',20,'男','信工',2)
laog.study(laoc)