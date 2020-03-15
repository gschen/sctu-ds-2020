class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def PersonInfo(self):
        print('我的姓名:%s,年龄:%s,性别:%s'%(self.name,self,age,self.gender))
class Teacher(Person):
    def __init__(self,name,age,gender,college,porfessional):
        super().__init__(name,age,gender)
        self.college=college
        self.porfessional=porfessional
    def PersonInfo(self):
        print('老师叫做%s,年龄:%s,性别：%s,他在%s学院，教%s'%(self.name,self.age,self.gender,self.college,self.porfessional))
    def TeachObj(self):
        return '今天讲了面向对象'
x=Teacher('王老师','30','男','信息与工程学院','数学')
x.PersonInfo()
print(x.TeachObj())