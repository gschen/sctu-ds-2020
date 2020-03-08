class Person(object):
    def personInfo(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex
a=Person()
print(a.personInfo('小明',18,'男'))