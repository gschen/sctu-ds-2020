class Student(Person):
    def _init_(self,name,age,sex,college,banji):
        super().college = college
        super().banji = banji

    def printInfo(self):
        print('我叫%s,年龄:%s,性别:%s,我是%s班的学生'%(self.name,self.age,self.sex,self.college,self.class))

    def learn(self,teacher):
        print('老师,%s,我终于学会了！'%(teacher.teach()))