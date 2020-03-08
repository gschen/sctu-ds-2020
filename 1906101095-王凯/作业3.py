import datetime
class student:
def __init__(self,Sno,Sname,Sbarthday,Sfaction):
self.Sage = 0
self.Sname = Sname
self.Sno = Sno
self.Sbarthday = datetime.datetime.strptime(Sbarthday,"%Y-%m-%d")
self.Sfaction = Sfaction
self.Setage(Sbarthday)
self.SetGarde(Sfaction)
def Setage(self,Sbarthday):
if (datetime.date.today().month - self.Sbarthday.month)>=0:
if (datetime.date.today().day - self.Sbarthday.day)<0 & (datetime.date.today().month - self.Sbarthday.month)==0:
self.Sage = datetime.date.today().year - self.Sbarthday.year -1
else:
self.Sage = datetime.date.today().year - self.Sbarthday.year
else:
self.Sage = datetime.date.today().year - self.Sbarthday.year -1
def SetGarde(self,Sfaction):

text1 = student('2018061','张三','1999-10-27',68)
print("学号：{0} 姓名：{1} 年龄：{2}  ".format(text1.Sno,text1.Sname,text1.Sage)) 
2. def __str__ (self):
        """ 对象返回值 """
        return '%s是%s%s的一位%d岁的%s同学'%(self.name,self.college,\
        self.banji,self.age,self.gender)
        
        
    
a=Student('小明',22,'男','家里蹲大学','三年二班')
a.personInfo()
a.study()
b=Student('小红',22,'女','家里蹲大学','三年二班')
b.personInfo()
c.personInfo()
a.study()
d=Teacher('小王',19,'男','家里蹲大学','屋里系')
d.personInfo()
for i in Student.data_student:
    print(i)

3.       
  
class Teacher(Person):
    """ 教师类 """
    
    def __init__ (self,name,age,gender,college,professional):
        """ 初始化教师类 """
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
        
    def personInfo (self):
        """ 打印教师信息 """
        super().personInfo()
        print('是%s%s的老师'%(self.college,self.professional))
        
    def teachObj (self):
        """ 讲课内容方法 """
        return '今天讲了如何用面向对象设计程序'
        
        
class Student(Person):
    """ 创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。重写__str__方法，返回student的信息 """
    data_student=[]
    
    def data (self):
        """ 学生数据列表方法 """
        Student.data_student.append('姓名:%s, 年龄:%d, 性别:%s, 学院:%s, 班级:%s'%(self.name,self.age,self.gender,self.college,self.banji))
    
    def __init__ (self,name,age,gender,college,banji):
        """ 初始化学生类 """
        super().__init__(name,age,gender)
        self.college=college
        self.banji=banji
        Student.data(self)
    
    def personInfo (self):
        """ 打印学生信息 """
        super().personInfo()
        print('是%s%s的学生'%(self.college,self.banji))
        
    def study (self):
        """ 学习的方法 """
        print('老师%s,我终于学会了！'%Teacher.teachObj(self))
        
    
————————————————
