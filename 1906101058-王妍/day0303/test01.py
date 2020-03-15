#第一题
class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def personInfo(self):
        print("姓名：%s,年龄：%s,性别:%s" % (self.name,self.age,self.sex))
a=Person('Bob',18,'男')
a.personInfo()
