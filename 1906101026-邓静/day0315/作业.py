#回合制人物PK游戏
import random
class Player():
    def __init__(self,name,attack,crit,dod):
        self.name=name
        self.blod=blod
        self.crit=crit
        self.dood=dood
    def role(self):
        print('玩家名称:%s\n血量:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.crit,self.dod))
a=Player('昭君',1500,200,0.1,0.3)
b=Player('婉儿',2000,200,0.2,0.1)
a.role()
b.role()

import random
class Player():
    def __init__(self,name,attack,crit,dod):
        self.name=name
        self.blod=blod
        self.crit=crit
        self.dood=dood
    def role(self):
        print('玩家名称:%s\n血量:%s\n暴击率:%s\n闪避率:%s' % (self.name,self.blood,self.attack,self.crit,self.dod))
class H():
    def __init__(self):
        self.player1=a
        self.player2=b
    def playgame(self):
        print('游戏开始')
        count=0
        while self.player1.blood>0 and self.player2.blood>0:
            count+=1
            if random.random()<=self.player1.crit:
                if random.random()<=self.player2.dod:
                    self.player2.blood -= 0
 				else:
 					self.player2.blood -= self.player1.attack * 2
 			else:
 				if random.random() <= self.player2.DOD:
 					self.player2.blood -= 0
 				else:
 					self.player2.blood -= self.player1.attack

 			if random.random() <= self.player2.crit:
 				if random.random() <= self.player1.DOD:
 					self.player1.blood -= 0
 				else:
 					self.player1.blood -= self.player2.attack * 2
 			else:
 				if random.random() <= self.player1.DOD:
 					self.player2.blood -= 0
 				else:
 					self.player1.blood -= self.player2.attack
 			if self.player1.blood <= 0:
 				self.player1.blood = 0
 			if self.player2.blood <= 0:
 				self.player2.blood = 0
 			print('第%d轮攻击:' % count)
 			print('昭君:剩余血量: %d' % self.player1.blood)
 		
 		
a=Player('昭君',1500,200,0.1,0.3)
b=Player('婉儿',2000,200,0.2,0.1)
 c=H()
 c.playGame()

