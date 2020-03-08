class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personlnfo(self):
        print('姓名：%s,年龄：%s,性别：%s'%(self.name,self.age,self.sex))
a=Person('李诗尧',18,'女')
a.personlnfo()
