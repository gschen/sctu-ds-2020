class Student():
    def __init__(self,name,age,cn_score,ma_score,eng_score):
        self.name=name
        self.age=age
        self.cn_score=cn_score
        self.ma_score=ma_score
        self.eng_score=eng_score
    def get_name(self):
        print("姓名:",self.name)
    def get_age(self):
        print("年龄:",self.age)
    def get_course(self):
        if type(self.cn_score) != int and type(self.ma_score) != int and type(self.eng_score) != int:
            print("错误的输入")
        else:
            print("语外数成绩:",self.cn_score,self.eng_score,self.ma_score)
l = Student("lz","19",80,80,80)
l.get_name()
l.get_age()
l.get_course()

1