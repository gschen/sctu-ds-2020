class Student(object):
    def __init__(self,name,age,score):
          self.name=name
          self.age=age
          self.score=score
    def get_name(self):
        if isinstance(self.name,str):
            return self.name
    def get_age(self):
        if isinstance(self.age,int):
            return self.age
    def get_course(self):
        a=max(self.score)
        if isinstance(a,int):
            return a

wwx=Student('王文星',18,[100,100,100])
print(wwx.get_name())
print(wwx.get_age())
print(wwx.get_course())

#猜拳游戏
import random
class Person():
    def __init__(self,name):
        self.name=name
        self.score=0
    
    def fingerPlay(self):
        game=['石头','剪刀','布']
        index=random.randint(0,2)
        #random.choice(game)
        return game[index]

class Game():
    def __init__(self,number,aname,bname):
        self.number=number
        self.a=Person(aname)
        self.b=Person(bname)
    
    def playGame(self):
        for i in range(self.number):
        a_out=self.a.fingerPlay()
        b_out=self.b.fingerPlay()
        
        if a_out==b_out:
            print('双方平局，出的是{}'.format(a_out))
        elif(a_out=='石头' and b_out=='剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='剪刀' and b_out=='布')：
            print('{}获得胜利，出的是{}，{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
        else:
            print('{}获得胜利，出的是{}，{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))

one=Game(5,'李靖','王妍')
one.playGame()