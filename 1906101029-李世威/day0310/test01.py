class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    def getMaxScore(self):
        print(max(self.score))

n = Student('lishiwei',19,[85,88,92])
n.getName()
n.getAge()
n.getMaxScore()