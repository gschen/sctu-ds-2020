#  创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class person():
    def personly(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        return self.name,self.age,self.sex

a=person()
print(a.personly('lisa','3岁','女'))
