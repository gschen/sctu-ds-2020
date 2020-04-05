#游戏：石头剪刀布
import random
class person():
    def __init__(self,name):
        self.name=name
        self.score=0
    
    def fingerplay(self):
        game=['石头','剪刀','布']
        index=random.randint(0,2)
        #random.choice(game)
        return game[index]

class game():
    def __init__(self,num,aname,bname):
        self.num=num
        self.a=person(aname)
        self.b=person(bname)

    def playgame(self):
        for i in range(self.num):
            a_out=self.a.fingerplay()
            b_out=self.b.fingerplay()
            if a_out==b_out:
                print('双方平局，出的是{}'.format(a_out))
            elif (a_out=='石头' and b_out=='剪刀') or (a_out=='布' and b_out=='石头') or (a_out=='剪刀' and b_out=='布'):
                self.a.score+=1
                print('{}获得胜利的是{}，{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                self.b.score+=1
                print('{}获得胜出,出的是{},{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
        if self.a.score>self.b.score:
            print('恭喜{}获得了胜利，得分{}'.format(self.a.name,self.a.score))
        elif self.a.scoree<self.b.score:
            print('恭喜{}获得了胜利，得分{}'.format(self.b.name,self.b.score))
        else:
            print('双方平局，不分胜负')

one=game(5,'梅梅','虾米')
one.playgame()