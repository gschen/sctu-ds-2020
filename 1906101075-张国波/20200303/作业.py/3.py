class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex 
    def personInfo(self):
        print('我叫%s,%s岁,性别:%s' % (self.name,self.age,self.sex))


class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name,age,sex)
        self.college = college
        self.professionaal = professional
    def personInfo(self):
        print('%s,%s,%s,%s,%s'%(self.name,self.age,self.sex,self.college,self.professionaal))
    def teachObj(self):
        return ('今天讲了：面向对象设计程序')


class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        super().__init__(name,age,sex)
        self.college = college
        self.banji = banji
    def personInfo(self):
        print('我叫%s,年龄:%s,性别:%s,学院:%s,班级:%s'%(self.name,self.age,self.sex,self.college,self.banji))
    def study(self,Teacher):
        print('老师%s,我终于学会了！'%(Teacher.teachObj(self)))
c=Student('张三',20,'男','信息与工程学院','2班')
c.personInfo()
c.study(Teacher)