class Student():
    def __init__(self,name,age,scores):
        self.__name=name
        self.__age=age
        self.__scores=scores
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_course(self):
        return max(self.__scores)
s=Student('huahua',18,[99,97,98])
print("姓名:%s"%(s.get_name()))
print("年龄:%s"%(s.get_age()))
print("最高分:%s"%(s.get_course()))
