class person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def printInfo(self):
        print('我叫%s,年龄：%s,性别:%s'%(self.name,self.age,self.sex))
