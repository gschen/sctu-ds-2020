class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex 
    def personInfo(self):
        print('我叫%s,%s岁,性别:%s' % (self.name,self.age,self.sex))
a=Person('ybr',19,'男')
a.personInfo()

#
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
        return ('今天讲了面向对象设计程序')
b=Teacher('cgs','40','男','信息与工程学院','计算机')
b.personInfo()
print(b.teachObj())

#
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
        return ('今天讲了面向对象设计程序')
