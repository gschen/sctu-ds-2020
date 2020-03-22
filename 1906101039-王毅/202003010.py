class Student():
    def __init__(self,name,age,chinese,math,english):
        self.name=name
        self.age=age
        self.chinese=chinese
        self.math=math
        self.english=english

    def p(self):
        print(self.name,self.age,self.chinese,self.math,self.english)
a=Student('王毅',19,150,150,150)
a.p()

import random
class Person():
    def __init__(self,name):
        self.name=name

    def fingerPlay(self):
        game=['石头','剪刀','布']
        index=random.randint(0,2)
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
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='剪刀' and b_out=='布') or(a_out=='布' and b_out=='石头'):
                print('{}获得胜利，出的是{},{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                print('{}获得胜利，出的是{},{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))

one=Game(5,'王毅','LYF')
one.playGame()
