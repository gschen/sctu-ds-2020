#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        #print(self.name,self.age,self.gender)
        print('我叫%s,年龄:%s,性别:%s'%(self.name,self.age,self.gender))
        #print('name=%s,age=%s,gender=%s'%(self.name,self.age,self.gender))

wang=Person('王二',20,'男')
wang.personInfo()