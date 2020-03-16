import random
class Person():
    def __init__(self,name):
        self.name = name
        self.score = 0
    def fingerplay(self):
        game = ['剪刀','石头','布']
        index = random.randint(0,2)
        return game[index]

class Game():
    def __init__(self,number,aname,bname):
        self.number = number
        self.a = Person(aname)
        self.b = Person(bname)
    def playGame(self):
        for i in range(self.number):
            a_out = self.a.fingerplay()
            b_out = self.b.fingerplay()

            if a_out == b_out:
                print ('双方平局，胜负不分，甲乙都出的%s' % (a_out))
            elif (a_out == '石头' and b_out == '剪刀') or (a_out == '剪刀' and b_out == '布') or (a_out == '布' and b_out == '石头'):
                self.a.score += 1
                print('%s赢了，%s出的%s' % (self.a.name,self.a.name,a_out))
            else:
                self.b.score += 1
                print('%s赢了，%s出的%s' % (self.b.name,self.b.name,b_out))
        if self.a.score == self.b.score:
            print('双方平局，胜负不分')   
        elif self.a.score > self.b.score:
            print('%s赢了，得分%s' % (self.a.name,self.a.score))
        else:
            print('%s赢了，得分%s' % (self.b.name,self.b.score))
a=Game(900,'甲','已')
a.playGame()


