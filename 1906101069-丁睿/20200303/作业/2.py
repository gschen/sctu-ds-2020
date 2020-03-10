class Person():
    def __init__(self,name,age,gender):
       self.name=name
       self.age=age
       self.gender=gender
    def personInfo(self):
        print('我的姓名：%s,年龄:%d,性别：%s'%(self.name,self.age,self.gender))
class Teacher(Person):
    def __init__(self,name,age,gender,college,perofessional):
        super().__init__(name,age,gender)
        self.college=college
        self.perofessional=perofessional
    def personInfo(self):
        print('老师叫做%s,年龄:%s,性别%s,他在%s学院，教%s'%(self.name,self.age,self.gender,self.college,self.perofessional))
    def teachObj(self):
        return '今天讲了面对对象'
b=Teacher('张三',36,'男','信息与工程学院','计算机')
b.personInfo()
print(b.teachobj())