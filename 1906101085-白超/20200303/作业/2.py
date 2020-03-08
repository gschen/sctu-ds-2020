class Teacher(Person):
    def _init_(self,name,age,sex,college,professional):
        super ()._init_(name,age,sex)
        self.college = college
        self.professional = professional
    
    def printInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是来自%s的一名%s讲师' % (self.name,self.age,self.sex,self.college,self.professional))

    def teach(self):
        return'今天讲了：面向对象设计程序'