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