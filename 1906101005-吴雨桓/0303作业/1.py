class Person():
    def __init__(self,name,age,sex):
        self.name = '吴雨桓'
        self.age = 19
        self.sex = '男'

    def personInfo(self):
        print('%s,年龄：%d，性别：%s'%(self.name,self.age,self.sex))

student=[]
a=Person('吴雨桓','19','男')
a.personInfo()


#第二题
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.collage=college
        self.professional=professional
    def printInfo(self):
        print('我叫：%s，年龄：%s，性别：%s，我是来自%s的一名%s讲师'%(self.name,self.age,self.sex,self.collage,self.professional))
    def teach(self):
        return '今天讲了如何面向对象设计程序'

teacher=Teacher('XX','xx','x','信息与工程学院','python')
teacher.printInfo()

#第三题
class Student(Person):
    def  __init__(self,name,age,sex,collage,clas):
        super().__init__(name,age,sex)
        self.collage=collage
        self.clas=clas
    def printInfo(self):
        print('我叫%s,年龄%s，性别%s，学院%s，班级%s'%(self.name,self.age,self.sex,self.collage,self.clas))
    def learn(self,teacher):
        print('我是%s，老师%s，我终于学会了'%(self.name,teacher.teach()))

student1 =Student('x','x','男','信息与工程学院','1901')
student1.printInfo()
student1.learn(teacher)






