class Student(object):
    def _init_(self,name,age,course):
        self._name = name
        self._age = age
        self._scores = scores
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_course(self):
        return max(self._scores)
Stu = Student('小明',18,[90,91,92])
print('姓名:%s'%(Stu.get_name()))
print('年龄:%s'%(Stu.get_age()))
print('最高分数:%s'%(Stu.get_course()))