#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print('姓名',self.name)
        print('年龄',self.age)
        print('性别',self.sex)
a=person('zh',19,'女')
a.personInfo()
