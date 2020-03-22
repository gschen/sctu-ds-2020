import random
import time
class Finger():
    def __init__(self,name,blood,atk,cri,evd):
        self.name = name
        self.blood = 150
        self.atk = 10
        self.cri = 0.3
        self.evd = 0.2
    
class Knight(Finger):
    def __init__(self,name = ['重装骑士——林']):
       
        self.blood = int(self.blood*1.5)
        self.atk = int(self.atk*1.2)
        self.cri = int(self.cri)
        self.evd = int(self.evd*1.1)

class Bowman(Finger):
    def __init__(self,name = ['暗月精灵——陈']):
        
        self.blood = int(self.blood)
        self.atk = int(self.atk*1.4)
        self.cri = int(self.cri*1.5)
        self.evd = int(self.evd*1.4)
    
class Game():
    def a_llll(self):
        self.players = []
        self.players.append(Knight(),Bowman())
    def PlayGame(self):
        for i in range(10):
            while self.players[0].blood > 0 and self.players[1].blood > 0:
                if i == 0 or i==2:
                    self.players[0].blood = self.players[0].blood - self.players[1].atk*2
                    time.sleep(1.5)
                    print('%sblood:%s.' % (self.players[0].name,self.players[0].blood))
                elif i == 3: 
                    self.players[1].blood = self.players[1].blood - self.players[0].atk*2
                    time.sleep(1.5) 
                    print('%sblood:%s.' % (self.players[1].name,self.players[1].blood))
                elif i == 1:
                    pass
                else:
                    self.players[0].blood = self.players[0].blood - self.players[1].atk
                    self.players[1].blood = self.players[1].blood - self.players[0].atk
                    time.sleep(1.5)
                    print('%sblood:%s.' % (self.players[0].name,self.players[0].blood))
                    print('%sblood:%s.' % (self.players[1].name,self.players[1].blood))
            if self.players[0].blood < 0 or self.players[0].blood == 0 and self.players[1].blood > 0:
                time.sleep(1.5)
                print('%s is the winner.' % (self.players[1].name))
            if self.players[1].blood < 0 or self.players[1].blood ==0 and self.players[0].blood > 0:
                time.sleep(1.5)
                print('%s is the winer.'% (self.players[0].name))



a=Game()











                


