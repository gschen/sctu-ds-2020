class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print('姓名:%s'%(self.name))
    def get_age(self):
        print('年龄:%d'%(self.age))
    def get_course(self):
        print('最高分：',max(self.score))
Y=Student('',18,[110,119,120])
Y.get_name()
Y.get_age()
Y.get_course()