class Student():
    def _init_(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        print(max(self.score))
m=Student("杨静",19,[98,95,99])
m.get_name()
m.get_age()
m.get_course()