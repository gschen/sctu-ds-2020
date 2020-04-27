class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personinfo(self):
        print(self.name)
        print(self.age)
        print(self.sex)

class Teacher(Person):
    def __init__(self,collage,professional):
        self.collage = collage
        self.professional = professional

    def personinfo(self):
        print(self.collage)
        print(self.professional)

    def teachojb(self):
        print('今天讲了：面向对象设计程序')

    def study(self,teacher):
        print('我是%s,老师%s,我终于学会了！')

