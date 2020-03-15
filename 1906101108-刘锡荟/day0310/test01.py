class student(object):
    def __init__(self,name,age,scores):
        self.__name=name
        self.__age=age
        self.__scores=scores
    def get__name(self):
        return self.__name
    def get__age(self):
        return self.__age
    def get__(self):
        return max(self.__scores)
stu = student('张三'，19，[82,84,86])
print('姓名：%s'%(stu.get__name()))       
print('年龄：%s'%(stu.get__age()))
print('最高分：%s'%(stu.get__course()))
