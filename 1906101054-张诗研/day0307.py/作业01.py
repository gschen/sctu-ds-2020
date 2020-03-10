#	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print("name:%s,age:%d,sex:%s"%(self.name,self.age,self.sex))
a=Person("Alice",19,"女")
a.personInfo()
