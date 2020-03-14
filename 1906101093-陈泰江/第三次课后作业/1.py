class Person():
    def __init__(self,name,age,sex,):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print('姓名',self.name)
        print('年龄',self.age)
        print('性别',self.sex)
Bob=Person('陈泰江',20,'男')
Bob.personinfo()