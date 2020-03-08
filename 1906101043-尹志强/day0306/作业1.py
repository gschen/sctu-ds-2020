class Person():
    def __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender=gender
    def personInfo(self):
        print('我的姓名：%s,年龄:%d,性别：%s'%(self.name,self.age,self.gender))
a=Person('尹志强',20,'男')
a.personInfo()
