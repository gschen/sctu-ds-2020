#1、创建Person类，属性有姓名、年龄、性别。创建方法personlnfo，打印这个人的信息

class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print(a.name,a.age,a.gender)
a=Person('和张艺',20,'男')
a.personInfo()