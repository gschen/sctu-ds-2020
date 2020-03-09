#2、创建Teacher类，继承Person类，属性有学院college，专业professional，
#重写父类personInfo方法，除打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了：面向对象设计程序’

class Techer(Person):
    def __init__(self,name,age,gender,college,professional):
        self.name=name  #super().__init__(name,age,gender)
        self.age=age    #可用这个调用作业1的代码，避免重复
        self.gender=gender
        self.college=college
        self.professional=professional
    def personInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是来自%s的一名%s老师'%(self.name,self.age,self.gender，self.college,self.professional))
    def teach(self):  
        return'今天讲了：面向对象设计程序'    