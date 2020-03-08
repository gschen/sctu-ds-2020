class Person:
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
    def personInfo(self):
        print("姓名：%s 年龄:%d 性别:%s"%(self.name,self.age,self.gender))
x = Person('张小明',48,'男')
x.personInfo()

   
        
