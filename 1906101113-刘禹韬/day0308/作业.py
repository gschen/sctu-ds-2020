class Person():
    def personinfo(self,mz,nl,xb):
        self.mz=mz
        self.nl=nl
        self.xb=xb
        return self.mz,self.nl,self.xb
class Teacher(Person):
    def personinfo(self,mz,nl,xb,xy,zy):
        self.mz=mz
        self.nl=nl
        self.xb=xb
        self.xy=xy
        self.zy=zy
        return self.mz,self.nl,self.xb,self.xy,self.zy
    def teachObj(self):
        return "今天讲了：面向对象设计程序"
class Student(Person):
    def personinfo(self,mz,nl,xb,xy,bj):
        self.mz=mz
        self.nl=nl
        self.xb=xb
        self.xy=xy
        self.bj=bj
        return self.mz,self.nl,self.xb,self.xy,self.bj
    def study(self,Teacher):
        return "老师%s，我终于学会了!"%Teacher.teachObj()
a=Student()
print(a.personinfo("张三","19","男","信工学院","信管"))
b=Teacher()
print(b.personinfo("李四","35","男","信工学院","信管"))
