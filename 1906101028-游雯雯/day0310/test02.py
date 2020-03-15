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
        self.number = number
        self.a = person()
        self.b = person()

    def playGame(self):
        for i in range(self.number):
            a_out=self.a.fingerPlay()
            b_Out=self.b.fingerPlay()
            if a_out == b_out:
                print('平局，出的是{}'.format(a_out))
            elif (a_out == '石头'and b_out == '剪刀')or(a_out == '布'and b_out == '石头')or(a__out == '剪刀'and b_out == '布'):
                print('{}获胜，出的是{},{}出的是{}'.format(self.a.name,a_out,self.b.name,b_out))
            else:
                print('{}获胜，出的是{},{}出的是{}'.format(self.b.name,b_out,self.a.name,a_out))
one = Game(5,'JYP','pupppy')
one.playGame()    