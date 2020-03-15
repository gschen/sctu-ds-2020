#类
'''
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return int(self.age)

    def get_course(self):
        # print(self.score.values())
        a = list(self.score.values())
        # print(a)
        return max(a)

student_01 = Student("马俊杰", 19, {'语文': 56, '数学': 100, '英语': 99})

print(student_01.get_name())
print(student_01.get_age())
print(student_01.get_course())
'''
#游戏
'''
import random
class Person():
    def __init__(self,name):
        self.name=name
    def fingerplay(self):
        game=['石头','剪刀','布']
        index=random.randint(0,2)
        #random.choice(game)
        return game[index]
    
class Game():
    def __init__(self,number):
        self.number=number
        self.a=a
        self.b=b
    def playgame(self):
        for i in range(self.number):
            a_out=self.a.fingerplay
            b_out=self.b.fingerplay
            if a_out==b_out:
                print('双方平局,出的是{}'.format(a_out))
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='剪刀' and b_out=='布'):
                print('{}获得胜利，出的是{},{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                print('{}获得胜利，出的是{},{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
            
one=Game(5)
'''
