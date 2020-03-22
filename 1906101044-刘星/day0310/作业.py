import random
class Person():
    def __init__(self,name,Blood,ATT,CRI,DOD):
        self.name=name
        self.Blood=Blood
        self.ATT=ATT
        self.CRI=CRI
        self.DOD=DOD
    def personinfo(self):
        print(('name:%s,Blood:%s,ATT:%s,CRI:%s,DOD:%s')%(self.name,self.Blood,self.ATT,self.CRI,self.DOD))
class Game():
    def __init__(self):
        self.playera=a
        self.playerb=b
    def playGame(self):
        print('游戏开始！')
        n=0
        while self.playera.Blood > 0 and self.playerb.Blood > 0:
            n += 1
            print('第%d轮攻击:' % n)
            if random.random() <= self.playerb.CRI:
                if random.random()<=self.playera.DOD:
                    self.playera.Blood == 0
                    print('{}的攻击被{}闪避'.format(self.playerb.name,self.playera.name))
                else:
                    self.playera.Blood == self.playerb.ATT*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.playerb.name,self.playerb.ATT*2))
            else:
                if random.random() <= self.playera.DOD:
                    self.playerb.Blood ==0
                    print('{}的攻击被{}闪避'.format(self.playera.name,self.playerb.name))
                else:
                    self.playera.Blood == self.playerb.ATT
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.playera.name,self.playera.ATT*2))
            if random.random()<=self.playera.CRI:
                if random.random() <= self.playerb.DOD:
                    self.playerb.Blood == 0
                    print('{}的攻击被{}闪避'.format(self.playera.name,self.playerb.name))
                else:
                    self.playerb.Blood == self.playera.ATT*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.playera.name,self.playera.ATT*2))
            else:
                if random.random() <= self.playerb.DOD:
                    self.playerb.Blood == 0
                    print('{}的攻击被{}闪避'.format(self.playerb.name,self.playera.name))
                else:
                    self.playerb.Blood == self.playera.ATT*2
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.playerb.name,self.playerb.ATT*2))
        if self.playera.Blood == 0:
            print('经过%d轮攻击，d成功击杀Lee，成为本局胜利者!' % n)
        else:
            print('经过%d轮攻击，e成功击杀Bob，成为本局胜利者!' % n)
a=Person('d',2000,100,0.5,0.3)
b=Person('e',2000,100,0.3,0.2)
c=Game()
c.playGame()