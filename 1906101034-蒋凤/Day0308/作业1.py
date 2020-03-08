#创建person类,属性有姓名、年龄、性别，创建方法，并打印。
class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personlnfo(self):
        print('%s,%d,%s'%(self.name,self.age,self.gender))
ppd=Person('小丸子',19,'女')
ppd.personlnfo()