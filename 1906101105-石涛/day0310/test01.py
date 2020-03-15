# coding=utf-8

'''练习：写一个类'''
class Student():
    def __init__(self,name,age,Chinese,math,English):
        self.name=name
        self.age=age
        self.Chinese=Chinese
        self.math=math
        self.English=English
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.Chinese,self.math,self.English)

st=Student('st',19,95,113,110)
print('姓名：',st.get_name())
print('年龄：',st.get_age())
print('最高成绩：',st.get_course())