class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def PersonInfo(self):
        print('我的姓名:%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender))
x=Person('赵燕',19,'女')
x.PersonInfo()