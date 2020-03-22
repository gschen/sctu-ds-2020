class Student():
    def __init__(self,name,age,chinese,math,english):
        self.name=name
        self.age=age
        self.chinese=chinese
        self.math=math
        self.english=english
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        print(max(self.chinese,self.math,self.english))
z=Student('lsy',18,85,86,88)
z.get_name()
z.get_age()
z.get_course()
