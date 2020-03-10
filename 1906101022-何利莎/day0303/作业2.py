class person():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def personinfo(self):
        print(h.name,h.age,h.sex)
h=person("lisa",19,"女")
h.personinfo()
class teacher(person):
    def __init__(self,college,major,teach):
        self.college=college 
        self.major=major
        self.teach=teach
    def personinfo(self):
        print(t.college,t.major)
    def teachobj(self):
        print(t.teach)
t=teacher("信息与工程学院","信息管理与信息系统","今天讲了，面向对象设计程序")
t.personinfo()
t.teachobj()