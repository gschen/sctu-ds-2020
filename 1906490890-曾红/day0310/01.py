# 定义一个学生student类,有以下属性：name,age,score, 
# 类的方法：1获取姓名：get name() 
#          2获取年龄：ge age()
#          3获取最高分：get score()

lass student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_score(self):
        print(max(self.score))
a=student('zh',19,[80,69,90])
a.get_age()
a.get_name()
a.get_score()



# class student():
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_score(self):
#         return max(self,_score)
# stu=student('zh',19,[57,89,46])
# print("姓名：%s"%(stu.get_name()))
# print("年龄：%s"%(stu.get_age()))
# print("最高分：%s"%(stu.get_score()))
