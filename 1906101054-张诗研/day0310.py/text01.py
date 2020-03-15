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
a=Student("bob",20,67,56,34)
a.get_name()
a.get_age()
a.get_course()