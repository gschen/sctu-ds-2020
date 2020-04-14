class Student(object):
    def __init__(self,name,age,sex,Englishscore,Mathscore,Chinesescore):
        self.name=name
        self.age=age
        self.sex=sex
        self.Englishscore=Englishscore
        self.Mathscore=Mathscore
        self.Chinesescore=Chinesescore
    def get_Student_Information(self):
        return self.name,self.age,self.sex
    def get_all_score(self):
        return self.Englishscore+self.Mathscore+self.Chinesescore
    def get_average_score(self):
        return (self.Englishscore+self.Mathscore+self.Chinesescore)/3

Jack=Student('Jack Smith',18,'男',100,100,100)
print('学生信息:%s,%s,%s'%(Jack.get_Student_Information()))
print('总成绩:%d'%(Jack.get_all_score()))
print('平均分:%d'%(Jack.get_average_score()))

