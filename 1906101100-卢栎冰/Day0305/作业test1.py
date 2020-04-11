# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person(object):
    def personInfo(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex
a=Person()
print(a.personInfo('小鹿','19','女'))
