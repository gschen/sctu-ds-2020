# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personInfo(self):
        print('我是%s,年龄:%d,性别:%s' % (self.name, self.age, self.sex))


stu1 = Person('张三',19, '男')
stu1.personInfo()

