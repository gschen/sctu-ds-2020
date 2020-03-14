#1创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息




class Person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
            print(a.name,a.age,a.sex)
a=Person("张三","20岁","男")
a.personInfo()