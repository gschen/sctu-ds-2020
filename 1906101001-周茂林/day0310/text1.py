class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.score)


a = Student("小明", 19, [90, 95, 100])
print(a.get_name())
print(a.get_age())
print(a.get_score())
