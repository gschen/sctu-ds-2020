#回合制人物Pk游戏
#创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
#创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame
#参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。
# 该方法打印每一轮游戏的情况，以及最终的获胜情况。
#备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
#if random.random() <= 0.2:
#	pass

import random
class Person():
    def __init__(self,name,blood,attack,crit,dodge):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.crit=crit
        self.dodge=dodge
    def personinfo(self):
        print(('角色名称:%s,角色血量:%s,攻击力:%s,暴击率:%s,闪避率:%s')%(self.name,self.blood,self.attack,self.crit,self.dodge))
class Game():
    def __init__(self):
        self.player1=a
        self.player2=b
    def playGame(self):
        print('游戏开始！')
        n=0
        while self.player1.blood>0 and self.player2.blood>0:
            n +=1
            print('第%d轮攻击:' % n)
            if random.random()<=self.player2.crit:
                if random.random()<=self.player1.dodge:
                    self.player1.blood -=0
                    print('{}的攻击被{}闪避'.format(self.player2.name, self.player1.name))
                else:
                    self.player1.blood -= self.player2.attack*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.player2.name,self.player2.attack*2))
            else:
                if random.random()<=self.player1.dodge:
                    self.player2.blood -=0
                    print('{}的攻击被{}闪避'.format(self.player1.name, self.player2.name))
                else:
                    self.player1.blood -= self.player2.attack
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.player1.name,self.player1.attack*2))
            if random.random()<=self.player1.crit:
                if random.random()<=self.player2.dodge:
                    self.player2.blood -=0
                    print('{}的攻击被{}闪避'.format(self.player1.name, self.player2.name))
                else:
                    self.player2.blood -= self.player1.attack*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.player1.name,self.player1.attack*2))
            else:
                if random.random()<=self.player2.dodge:
                    self.player2.blood -=0
                    print('{}的攻击被{}闪避'.format(self.player2.name, self.player1.name))
                else:
                    self.player2.blood -= self.player1.attack*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.player2.name,self.player2.attack*2))
        if self.player1.blood == 0:
            print('经过%d轮攻击，Bob成功击杀Lee，成为本局胜利者!' % n)
        else:
            print('经过%d轮攻击，Lee成功击杀Bob，成为本局胜利者!' % n)
a=Person('Lee',20000,1000,0.4,0.3)
b=Person('Bob',20000,1100,0.3,0.2)
yi=Game()
yi.playGame()
