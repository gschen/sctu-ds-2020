#HP=血量，CE=伤害，AVD:闪避率，CRT：暴击率
import random
class Player():
    def __init__(self,name,HP,CE,AVD,CRT):
        self.name=name
        self.HP=HP
        self.CE=CE
        self.AVD=AVD
        self.CRT=CRT
    def figure(self):
        print('玩家名称:%s\nHP:%s\nCE:%s\nAVD:%s\nCRT:%s'%(self.name,self.HP,self.CE,self.AVD,self.CRT))
a=Player("JOJO",200,15,0.5,0.9)
b=Player("DIO",300,10,0.6,0.4)
         
a.figure()
b.figure()

class Game():
    def __init__(self):
        self.player1=a
        self.player2=b
    def playerGame(self):
        print('Game Start')
        count=0
        while self.player1.HP>0 and self.player2.HP>0:
            count+=1
            if random.random() <= self.player1.CRT:
                if random.random() <= self.player2.AVD:
                    self.player2.HP-=0
                else:
                    self.player2.HP -= self.player1.CE*2
            else:
                if random.random() <= self.player2.CRT:
                    self.player2.HP-=0
                else:
                    self.player2.HP -= self.player1.CE
            if random.random() <= self.player2.AVD:
                if random.random()<=self.player1.CRT:
                    self.player1.HP-=0
                else:
                    self.player1.HP -= self.player2.CE*2
            else:
                if random.random() <= self.player1.CRT:
                    self.player2.HP-=0
                self.player1.HP -= self.player2.CE
            if self.player1.HP<=0:
                self.player1.HP=0
            print('JOJO:剩余血量:%d'% self.player1.HP)
            if self.player2.HP<=0:
                self.player2.HP=0
            print('第%d轮攻击:'% count)
            print('DIO:剩余血量:%d'% self.player2.HP)
        if self.player1.HP==0:
            print('Game Over,JOJO is Winner')
        else:
            print('Game Over ,DIO is Winner')
a=Player("JOJO",200,15,0.5,0.9)
b=Player("DIO",300,10,0.6,0.4)    
H=Game()
H.playerGame()              


