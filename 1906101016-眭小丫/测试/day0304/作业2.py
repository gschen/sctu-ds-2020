#2、创建Teacher类，继承Person类，属性有学院college，专业professional
#，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’
class Person(object):
    def _init_(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personInfo(self):
        print('我叫%s,年龄:%d,性别:%s'%(self.name,self.age,self.gender))

class Teacher(Person):
    def _init_(self,name,age,gender,college,personInfo):
        super()._init_(name,age,gender)
        self.college=college
        self.personInfo=personInfo
    #def personInfo(self):
        super().personInfo()
        print('是%s%s的老师'%(self.college,self.personInfo))
    def teachobj(self):
        return '今天讲了：面向对象程序设计'

