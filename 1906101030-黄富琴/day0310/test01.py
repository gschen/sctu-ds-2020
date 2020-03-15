class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.score)
a=Student('张三',18,[70,80,90])
print('姓名:%s'%(a.get_name()))
print('年龄:%s'%(a.get_age()))
print('最高分:%s'%(a.get_course()))