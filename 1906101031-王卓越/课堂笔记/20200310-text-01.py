class Student:
    name='张三'
    age=18
    score_chinese=60
    score_math=70
    score_english=80
    
    @classmethod
    def get_name(cls):
        print(cls.name)
    @classmethod
    def get_age(cls):
        print(cls.age)
    @classmethod
    def get_course(cls):
        print(max(cls.score_chinese,cls.score_english,cls.score_math))

import random
class Person:
    def __init__(self,name):
        self.name=name
        self.sorce=0
    def fingerPlay(self):
        game=['石头','剪刀','布']
        index=random.choice(game)
        return index

class Game():
    def __init__(self,number,a,b):
        self.number=number
        self.a=Person(a)
        self.b=Person(b)
    def playGame(self):
        for i in range(self.number):
            a_out=self.a.fingerPlay()
            b_out=self.b.fingerPlay()
            if a_out==b_out:
                print('平局，出的是{}'.format(a_out))
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='剪刀' and b_out=='布') or (a_out=='布' and b_out=='石头'):
                self.a.sorce+=1
                print('赢的是{}，出的是{}，输的是{}，出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                self.b.sorce+=1
                print('赢的是b，出的是{}, 输的是{}，出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
    def sorce(self):
        print('{}的最终得分为{}，{}的最终得分为{}'.format(self.a.name,self.a.sorce,self.b.name,self.b.sorce))
if __name__=='__main__':
    f=Game(3,'张三','李四')
    f.playGame()
    f.sorce()