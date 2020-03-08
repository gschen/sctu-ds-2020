# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息

class person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('姓名:%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender)) 
胡艳萍=person('胡艳萍',18,'女')
胡艳萍.personInfo()