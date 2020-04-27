class Person():
    def __init__(self,name,ages,sex):
        self.name = name
        self.ages = ages
        self.sex  = sex
    def personInfo(self):
        print("姓名:",self.name)
        print("年龄:",self.ages)
        print("性别:",self.sex)
jams=Person("jams",18,"男")
jams.personInfo()