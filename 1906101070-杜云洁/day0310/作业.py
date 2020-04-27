# 回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避
# ----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。
# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass

import random
class Character():
    def __init__(self,name,blood,attack,violence,dodge):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.violence=violence
        self.dodge=dodge
    def information(self):
        print('玩家名称:%s 血量:%s 攻击力:%s 暴击率:%s 闪避率:%s'%(self.name,self.blood,self.attack,self.violence,self.dodge))
        
        
class Game():
    def __init__(self):
        self.player1=a
        self.player2=b
     
        
    def play(self):
        s=0
        while self.player1.blood>0 and self.player2.blood>0:
            s+=1
            if random.random()<self.player1.violence:
                if random.random()<=self.player2.dodge:
                    self.player2.blood-=0
                else:
                    self.player2.blood-=self.player1.attack*2
            else:
                if random.random()<=self.player2.dodge:
                    if random.random()<=self.player1.dodge:
                        self.player2.blood-=0
                    else:
                        self.player1.blood-=self.player2.attack
                if self.player1.blood<=0:
                    self.player1.blood=0
                if self.player2.blood<=0:
                    self.player2.blood=0
                print('第%d轮攻击:'%s)
                print('A:剩余血量%d'%self.player1.blood)
                print('B:剩余血量%d'%self.player2.blood)
            if self.player1.blood==0:
                print('经过%d轮,A获得胜利'% s)
            else:
                print('经过%d轮,B获得胜利'% s)
a=Character('A',100,100,0.4,0.3)
b=Character('B',100,100,0.2,0.1)
c=Game()
c.play()
        