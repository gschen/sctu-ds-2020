class Person():
    def __init__(self):
        self.name='常琳'
        self.age=19
        self.sex='女'
        self.college='四川旅游学院'
        self.profession='信息管理与信息系统'
    def Personinfo(self):
        print('name:{},age:{},sex:{},college:{},profession:{}'.format(self.name,self.age,self.sex,self.college,self.profession))
class Teach():
    def __init__(self):
        Person.__init__(self)
        self.today='今天讲了，面向对象编程'
    def teachobj(self):
        return self.today
a=Teach()
b=Person()
print(b.Personinfo())
print(a.teachobj())

