class Student():
    #def __init__(self,name,age,yuwen,shuxue,yingyu):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        # self.yuwen=yuwen
        # self.shuxue=shuxue
        # self.yingyu=yingyu
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        #print(self.yuwen,self.shuxue,self.yingyu) 
        #print(max(self.yuwen,self.shuxue,self.yingyu))
        print(max(self.score))
z=Student('zouting',20,[85,86,87])
z.get_name()
z.get_age()
z.get_course()
