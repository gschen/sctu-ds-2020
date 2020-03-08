#1、	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,name,age,sex,):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print(self.name,self.age,self.sex)
a=Person('李世威',19,'男')
a.personinfo()