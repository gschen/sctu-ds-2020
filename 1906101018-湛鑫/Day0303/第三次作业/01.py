# 1、	创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息

class Person():
    def __init__(self,name,age,gender):
        self.name="湛鑫"
        self.age="18岁"
        self.gender="女"
    def personInfo(self):
            print(a.name,a.age,a.gender)
a=Person("湛鑫","18岁","女")
