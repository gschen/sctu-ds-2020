#2、创建Teacher类，继承Person类，属性有学院college，专业professional
#，重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

class Teacher(object):
    def _init_(self,name,age,gender,college,personInfo):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.personInfo=personInfo
    #def personInfo(self):
        print('%s,%d,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.personInfo))
    def teachobj(self):
        print('今天讲了：面向对象程序设计')
zs=Teacher('张三','20','女','sctu','食品')
zs.personInfo()
zs.teachobj
