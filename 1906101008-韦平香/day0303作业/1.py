#1、	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,李小,age,男):
        self.x='李小'
        self.y=18
        self.z='男'
    def f1(self):
        a=self.x+self.y+self.z
        return a
