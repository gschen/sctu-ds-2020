class Person(object):
    def personInfo(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex
class Teach(Person):
    def personInfo(self,name,age,sex,college,professional):
        self.name=name
        self.age=age
        self.sex=sex
        self.college=college
        self.professional=professional
        return self.name,self.age,self.sex,self.college,self.professional
    def teachObj(self):
        return '今天讲了：面向对象设计程序'
a=Teach()
print(a.personInfo('小明',18,'男','战神学院','剑术'))
print(a.teachObj())