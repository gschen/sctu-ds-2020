class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.scores)
stu = Student('慕斯', 18, [110, 90, 91])
print("姓名：%s"%(stu.get_name()))
print("年龄：%s"%(stu.get_age()))
print("最高分：%s"%(stu.get_score()))

