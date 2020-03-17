class Student():
    def __init__(self,name,age,score,Chinese,Math,English):
        self.name=name
        self.age=age
        self.score=score
        self.Chinese=Chinese
        self.Math=Math
        self.English=English
    def get_name(self):
        print('姓名:',self.name)
    def get_age(self):
        print('年龄:',self.age)
    def get_Chines_and_Math_and_English(self):
        print('语文：%s  数学：%s  英语：%s'%(self.Chinese,self.Math,self.English))
    def get_score(self):
        print("最高分:%s"%( max(self.score)))
st=Student('张三',19,[91,82,86],'91','82','86')
st.get_name()
st.get_age()
st.get_Chines_and_Math_and_English()
st.get_score()
