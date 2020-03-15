# 一、定义一个学生Student类。有下面的类属性: 
# 1姓名name;
# 2年龄age
# 3成绩score (语文，数学，英语) [每课成绩的类型为整数]
# 类方法:
# 1获取学生的姓名: get name()
# 2获取学生的年龄: get age()
# 3返回3门科目中最高的分数。get course()
class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print('姓名：',self.name)
    def get_age(self):
        print('年龄：',self.age)
    def get_score(self):
        print('最高分：',max(self.score))

x=Student('张三',20,[80,90,95])
x.get_name()
x.get_age()
x.get_score()
       
