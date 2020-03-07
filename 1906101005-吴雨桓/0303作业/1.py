class Person():
    def __init__(self,name,age,sex):
        self.name = '吴雨桓'
        self.age = 19
        self.sex = '男'

    def personInfo(self):
        print('%s,年龄：%d，性别：%s'%(self.name,self.age,self.sex))

student=[]
a=Person('张三','18','男')
a.personInfo()






