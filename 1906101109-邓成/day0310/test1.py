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

n = Student('小黑',19,[77,88,99])
n.getName()
n.getAge()
n.getMaxScore()
