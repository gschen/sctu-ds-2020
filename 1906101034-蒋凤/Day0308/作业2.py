class Teacher(object):
    def __init__(self,name,age,gender,college,professional):
        self.name=name
        self.age=age
        self.gender=gender
        self.college=college
        self.professional=professional
    def personlnfo(self):
        print('%s,%d,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.professional))
    def teachObj(self):
        print('今天讲了：面向对象设计程序')
xiaowanzi=Teacher('小丸子',19,'女','sctu','信管')
xiaowanzi.personlnfo()
xiaowanzi.teachObj()

