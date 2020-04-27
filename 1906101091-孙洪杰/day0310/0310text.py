class Student():
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
s=Student("王小明",18,[90,99,80])
s.get_name()
s.get_age()
s.get_score()


import random
class Person():
    self.name=name

    def fingerPlay(self):
        game=['石头','剪刀','布']
        index-random.randint(0,2)
        #random.choice(game)
        return game[index]

class Game():
    def __init__(self,number):
        self.number=number
        self.a=Person()
        self.h=Person()

def playGame(self):
    for i in range(self.number):
        a_out=self.a.fingerPlay()
        b_out=self.b.fingerPlay()
        if a_out==b_out:
            print('双方平局，出的是{}'.dormat(a_out))
        elif (a_out=='石头' and b_out=='剪刀')or(a_out=='布' and b_out=='石头')or(a_out=='剪刀' and b_out=='布'):
            self.a.score+=1
            print('{}获得胜利，出的是{}，{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out)
        else:
            print('{}获得胜利，出的是{}，{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out)
            self.b.score+=1
    if  self.a.score>self.b.score:
        print( '恭喜{}获得游戏胜利，得分{}' .format(self . a. name, self .a. score))
    elif self.a.score<self.b.score:
        print('恭喜{}获得游戏胜利，得分{}'. format(self . b. name , self .b. score)
    else:
        print('双方平局，不分胜负')

one=Game(5)
one.playGame()

