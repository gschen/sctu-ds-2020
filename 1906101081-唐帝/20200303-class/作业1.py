class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('我叫%s,年龄:%s,性别%s' % (self.name,self.age,self.sex))
xiaoming=Person('唐帝',19,'男')
xiaoming.personInfo()
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.collage=college
        self.professional=professional
    def printInfo(self):
        print('我叫：%s，年龄：%s，性别：%s，我是来自%s的一名%s讲师'%(self.name
                                                 ,self.age,self.sex,self.collage,self.professional))
    def teach(self):
        return '今天讲了如何面向对象设计程序'
class Student(Person):
    def  __init__(self,name,age,sex,collage,banji):
        super().__init__(name,age,sex)
        self.collage=collage
        self.banji=banji
    def printInfo(self):
        print('我叫%s,年龄%s，性别%s，学院%s，班级%s'%(self.name,self.age,self.sex,self.collage,self.banji))
    def learn(self,teacher):
        print('我是%s，老师%s，我终于学会了'%(self.name,teacher.teach()))


#。。。