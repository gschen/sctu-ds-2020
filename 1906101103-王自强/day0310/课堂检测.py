class Student(object):
    def __int__(self,name,age,sore_math,sore_ch,sore_en):
        self.name=name
        self.age=age
        self.sore=[sore_math,sore_ch,sore_en]
        return self.name,self.age,self.sore
    def get_name(self):
        print(x.name)
    def get_age(self):
        print(x.age)
    def get_course(self):
        print('sore_math={},sore_ch={},sore_en={}'.format(x.sore[0],x.sore[1],x.sore[2]))
x=Student()
x.name='xiaoming'
x.age=18
x.sore=[88,99,78]
x.get_name()
x.get_age()
x.get_course()