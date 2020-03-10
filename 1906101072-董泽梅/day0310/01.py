class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        print(max(self.score))
my_info=Student('dzm',19,[58,59,61])
my_info.get_name()
my_info.get_age()
my_info.get_course()





