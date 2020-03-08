#01
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex =sex
    def printInfo(self):
        print('他叫%s,年龄:;%s,性别:%s'%(self.name,self.age,self.sex))

class Student(Person):
    def __init__(self,name,age,sex,collage,banji):
        super().__init__(name,age,sex)
        self.collage = collage
        self.banji = banji

    def printInfo(self):
        print('他叫%s,年龄:%s,性别:%s,是%s的%s班的学生'%(self.name,self.age,self.sex,self.collage,self.banji))


#02
def printInfo(self):
    print('我叫%S，年龄: %S，性别: %S ，我是来自%S的一名%s讲师'%(self. name,self. age, self. sex,self. college，self. professional))

def teach(self):
    return '今天讲了：如何用面向对象设计程序'

student = []
stu = Person('张三’，'18'，'男')
stul = Person('李四','19','男'）
stu2 = Person('小何’，'20',女')

student3 = Student('张三'，'18','男'，'信息工程院')
student1 = Student('李四' ，'19''男'，'信息工程院')
student2 = Student( '小何' ,'20’，‘信息工程院’
teacher = Teacher('王昀东' ，'30'，'男','信息工程院','python'
                  
stu. printInfo()
stu1.printInfo()
stu2 .printInfo()

student3.printInfo()
student1.printInfo()

student2.printInfo()
teacher.printInfo()

student3.Learn(teacher )
studentl.learn( teacher
student2.learn(teacher)

student1.addStudent( )
student2.addStudent()

student3.addStudent( )
Student.show_ all()



#03
def learn(self, teacher):
    print("我是%s,老师，%s ,我终于学会了!"%(self.name,teacher.teach()))

def addStudent(self):
    coutent = {}
    coutent['name'] = self.name
    coutent['age'] = self.age
    coutent['sex'] = self.sex
    coutent['collage'] = self.colleag
    student.append(coutent)

def show_all():
    for dict in student:
        for key in dict.keys():
            if key == 'name':
                print('姓名:'+dict[key])
            if key == 'age':
                print('年龄:'+dict[key])
            if key == 'sex':
                print('性别:'+dict[key])
            if key == 'collage':
                print('学院:'+dicr[key])
            if key == 'banji‘:
                print('班级:'+dict[key])

def __str__(self):
    msg = '我叫%s,年龄:%s,性别:%s,是%s的%s班的学生'
    return msg

class Teacher(Person):
    def __init__(self,name,age,sex,collage,professional):
        super().__init__(name,age,sex)
        self.collage = collage
        self.professional = prpfessional
    