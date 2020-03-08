#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person(object):
    def _init_(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(m.name,m.age,m.gender)
m=Person("小明","16岁","男")
m.personInfo()
