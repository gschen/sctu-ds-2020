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
        list1=[]
        list1.append(self.chinese)
        list1.append(self.math)
        list1.append(self.english)
        print(max(list1))
yi=Student("Lee",19,90,95,90)
yi.get_name()
yi.get_age()
yi.get_course()
