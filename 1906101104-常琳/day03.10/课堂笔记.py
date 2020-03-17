#定义一个学生类，姓名，年龄，语文，数学，英语
#类方法：获取姓名、年龄、三科成绩中的最高分

class Student():
    def __init__(self,name,age,Chinese,math,English):
        self.name=name
        self.age=age
        self.Chinese=Chinese
        self.math=math
        self.English=English
    def studentinfo(self):
        return (self.name,self.age)
    def get_course(self):
        return max(self.Chinese,self.math,self.English)
a=Student('常琳',19,89,88,87)
print("个人信息:",a.studentinfo())
print('最高成绩：',a.get_course())









