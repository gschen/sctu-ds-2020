
class Student():
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_course(self):
        return max(self.__scores)
zy=Student('赵颖',19,[91,92,93])
print("姓名：%s"%(zy.get_name()))
print("年龄：%s"%(zy.get_age()))
print("最高分：%s"%(zy.get_course()))


    