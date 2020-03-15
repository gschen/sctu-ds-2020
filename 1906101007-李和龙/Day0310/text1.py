class Student():
    def __init__(self,name,age,math_score,chinese_score,english_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.chinese_score = chinese_score
        self.english_score = english_score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max[int(self.math_score),self.english_score,self.chinese_score]

student = Student("小明","19",19,30,28)
print(student.get_name())
print(student.get_age())

print(student.get_course())

