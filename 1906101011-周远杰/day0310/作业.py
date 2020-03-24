# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass



import random
class Player():
    def __init__(self,name,blood,attack,crit,DOD):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.crit=crit
        self.DOD=DOD
    def role(self):
        print('玩家名称:%s\n血量:%s\n攻击力:%s\n暴击率:%s\n闪避率:%s'%(self.name,self.blood,self.attack,self.crit,self.DOD))
a=Player('林以信',3000,999,0.9,0.9)
b=Player('林以北',3000,100,0.2,0.2)
a.role()
b.role()
class Game():
    def __init__(self):
        self.player1=a
        self.player2=b
    def playerGame(self):
        print('游戏开始')
        count=0
        while self.player1.blood>0 and self.player2.blood>0:
            count+=1
            if random.random() <= self.player1.crit:
                if random.random() <= self.player2.DOD:
                    self.player2.blood-=0
                else:
                    self.player2.blood -= self.player1.attack*2
            else:
                if random.random() <= self.player2.DOD:
                    self.player2.blood-=0
                else:
                    self.player2.blood -= self.player1.attack
            
            if random.random() <= self.player2.crit:
                if random.random()<=self.player1.DOD:
                    self.player1.blood-=0
                else:
                    self.player1.blood -= self.player2.attack*2
            else:
                if random.random() <= self.player1.DOD:
                    self.player2.blood-=0
                else:
                    self.player1.blood-=self.player2.attack
            if self.player1.blood<=0:
                self.player1.blood=0
            if self.player2.blood<=0:
                self.player2.blood=0
            print('第%d轮攻击:'% count)
            print('林以信:剩余血量:%d'% self.player1.blood)
            print('林以北:剩余血量:%d'% self.player2.blood)
        if self.player1.blood==0:
            print('经过%d轮攻击,林以北成功击杀林以信,成为本局胜利者.'% count)
        else:
            print('经过%d轮攻击，林以信成功击杀林以北,成为本局胜利者.'% count)
a=Player('林以信',3000,999,0.9,0.9)
b=Player('林以北',3000,100,0.2,0.2)
c=Game()
c.playerGame()
