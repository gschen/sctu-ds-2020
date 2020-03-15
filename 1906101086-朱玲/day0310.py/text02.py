import random
class Person():
    def _init_(self,name):
        self.name=name
        self.score=0

    def fingerplay(self):
        game=['石头','剪刀','布']
        index=random.randint(0,2)
        return game[index]

class Game():
    def _init_(self,number,aname,bname):
        self.Number=Number
        self.a=Person(aname)
        self.b=Person(bname)

    def playGame(self):
        for i in range(self.number):
            a_out=self.a.fingerPlay()
            b_out=self.b.fingerPlay()
            
            if a_out==b_out:
                 (a_out=='双方平局，都出了{}'.format(a_out))
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='剪刀' and b_out=='布'):
                print('{}获胜，出了{},{}出了{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                self.a.score+=1
                print('{}获胜，出了{},{}出了{}'.format(self.a.name,a_out,self.b.name,b_out))
        if self.a.score>self.b.score:
            print('恭喜{}获胜，得分{}'.format(self.a.name,self.a.score))
        elif self.a.sore<self.b.score:
            print('{}获胜，出了{},{}出了{}'.format(self.b.name,b_out,self.a.name,a_out))
        else:
            print('双方平局')
one=Game(600,'小明','小红')
one.playGame()