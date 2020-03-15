# 1、	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person:
     def __init__(self,name,age,sex):
         self.name=name
         self.age=age
         self.sex=sex
     def personInfo(self):
        print('姓名:%s,年龄:%s,性别:%s'%(self.name,self.age,self.sex))
 Person.name=input('请输入姓名:')
 Person.age=input('请输入年龄:')
 Person.sex=input('请输入性别:') 