class Person():
    def __init__(self):
        self.name = "吴云康"
        self.age = 20
        self.gender = "male"
        self.college = "信息与工程学院"
        self.professional = "信息管理与信息系统"
    def personInfo(self):
        return "name:{},age:{},gender:{},college:{},professional:{}".format(self.name,self.age,self.gender,self.college,self.professional)