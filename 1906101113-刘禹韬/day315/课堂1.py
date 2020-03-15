class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getMaxScore(self):
        return max(self.score)

s=Student('学生',19,[59,60,61])
print(s.getName())
print(s.getAge())
print(s.getMaxScore())
