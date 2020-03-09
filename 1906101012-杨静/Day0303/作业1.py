# 创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息


class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
            print(a.name,a.age,a.gender)
a=Person("李四","18岁","男")
a.personInfo()     