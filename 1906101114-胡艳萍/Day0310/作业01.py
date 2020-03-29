import random

class Character():
    def __init__(self,name,blood,attack,crit,dodge):
        self.name=name
        self.blood=blood
        self.attack=attack
        self.crit=crit
        self.dodge=dodge
class Game():
    def __init__(self,character_a,character_b):
        self.a=character_a
        self.b=character_b
    def playgame(self):
        n = 1
        while self.a.blood > 0 and self.b.blood > 0:
            c = input('游戏开始：')
            print('第{}回合开始'.format(n))
            a=1
            b=1
            while a == 1:
                if random.random() <= self.b.dodge:
                    print('{}的攻击被{}闪避'.format(self.a.name, self.b.name))

                elif random.random() <= self.a.crit:
                    print('{}暴击，造成了{}点伤害'.format(self.a.name,self.a.attack*2))
                    self.b.blood -= self.a.attack*2
                else:
                    print('{}攻击，造成了{}点伤害'.format(self.a.name,self.a.attack))
                    self.b.blood -= self.a.attack
                a = 0
            while b == 1:
                if random.random() <= self.a.dodge:
                    print('{}的攻击被{}闪避'.format(self.b.name, self.a.name))
                elif random.random() <= self.b.crit:
                    print('{}暴击，造成了{}点伤害'.format(self.b.name,self.b.attack*2))
                    self.a.blood -= self.b.attack*2
                else:
                    print('{}攻击，造成了{}点伤害'.format(self.b.name,self.b.attack))
                    self.a.blood-= self.b.attack
                b = 0
            print('第{}回合结束，{}剩余{}点血量，{}剩余{}点血量'.format(n,self.a.name,self.a.blood,self.b.name,self.b.blood))
            n += 1
        if  self.a.blood < 0 and self.b.blood > 0:
            print('{}获得胜利，游戏结束'.format(self.b.name))
        elif  self.a.blood > 0 and self.b.blood < 0:
            print('{}获得胜利，游戏结束'.format(self.a.name))
        else:
            print('双方平手，游戏结束')

a = Character('玩家1',100,10,0.2,0.15)
b = Character('玩家2',100,20,0.1,0.25)
game=Game(a,b)
game.playgame()
