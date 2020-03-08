class Person():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex 
    def personInfo(self):
        print('我叫%s,%s岁,性别:%s' % (self.name,self.age,self.sex))
a=Person('张三',20,'男')
a.personInfo()