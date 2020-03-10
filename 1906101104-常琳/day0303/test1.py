class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print("个人信息：姓名：%s,年龄：%s,性别：%s"%(self.name,self.age,self.sex))
a=Person("常琳",19,"女")
a.personinfo()
