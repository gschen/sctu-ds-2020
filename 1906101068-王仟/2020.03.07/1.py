class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def personInfo(self):
        print("姓名：%s,年龄:%s,性别:%s" % (self.name,self.age,self.gender))
a=Person('王仟',20,'女')
a.personInfo()