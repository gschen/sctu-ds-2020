import random
class Gameperson():
    def __init__(self,name,blood,aggressivity,violence,dodge):
        self.name = name
        self.blood = blood
        self.aggressivity = aggressivity
        self.violence = violence
        self.dodge = dodge
    def information(self):
        print('玩家名称：%s\n血量：%s\n攻击力：%s\n暴击率：%s\n闪避率：%s' % (self.name,self.blood,self.aggressivity,self.violence,self.dodge))


class Chuanqi():
    def __init__(self):
        self.player1 = a
        self.player2 = b
    def playGame(self):
        global xx1 
        global xx2
        global yy1
        global yy2
        global injure1
        global injure2
        global injured1
        global injured2
        print('游戏开始！')
        count = 0
        while self.player1.blood>0 and self.player2.blood>0:
            count += 1
            if random.random()<=self.player1.violence:
                if random.random()<=self.player2.dodge:
                    xx2 = '闪避'
                    yy1 = '未击中'
                    injure1 = 0
                    injured2 = 0
                    self.player2.blood -= 0
                else:
                    xx2 = '被击中'
                    yy1 = '产生暴击'
                    if self.player1.aggressivity * 2>self.player2.blood:
                        injure1 = self.player2.blood
                        injured2 = self.player2.blood
                    else:
                        injure1 = self.player1.aggressivity * 2
                        injured2 = self.player1.aggressivity * 2
                    self.player2.blood -= self.player1.aggressivity * 2
            else:
                if random.random()<=self.player2.dodge:
                    self.player2.blood -= 0
                    xx2 = '闪避'
                    yy1 = '未击中'
                    injure1 = 0
                    injured2 = 0
                else:
                    xx2 = '被击中'
                    yy1 = '未暴击'
                    injure1 = self.player1.aggressivity
                    injured2 = self.player1.aggressivity
                    self.player2.blood -= self.player1.aggressivity
            if random.random()<=self.player2.violence:
                if random.random()<=self.player1.dodge:
                    xx1 = '闪避'
                    yy2 = '未击中'
                    injure2 = 0
                    injured1 = 0
                    self.player1.blood -= 0
                else:
                    xx1 = '被击中'
                    yy2 = '产生暴击'
                    if self.player2.aggressivity * 2>self.player1.blood:
                        injure2 = self.player1.blood
                        injured1 = self.player1.blood
                    else:
                        injure2 = self.player2.aggressivity * 2
                        injured1 = self.player2.aggressivity * 2
                        self.player1.blood -= self.player2.aggressivity * 2
            else:
                if random.random()<=self.player1.dodge:
                    xx1 = '闪避'
                    yy2 = '未击中'
                    injure2 = 0
                    injured1 = 0
                    self.player2.blood -= 0
                else:
                    xx1 = '被击中'
                    yy2 = '未暴击'
                    injure2 = self.player2.aggressivity
                    injured1 = self.player2.aggressivity
                    self.player1.blood -= self.player2.aggressivity
            if self.player1.blood<=0:
                self.player1.blood = 0
            if self.player2.blood<=0:
                self.player2.blood = 0
            print('第%d回合：' % count)
            print('%s：%s 受到伤害：%d;%s 产生伤害：%d\n剩余血量：%d' % (self.player1.name,xx1,injured1,yy1,injure1,self.player1.blood))
            print('%s：%s 受到伤害：%d;%s 产生伤害：%d\n剩余血量：%s' % (self.player2.name,xx2,injured2,yy2,injure2,self.player2.blood))
        if self.player1.blood == 0:
            print('经过%d回合游戏，%s成功击杀%s，成为本局游戏的胜利者。' % (count,self.player2.name,self.player1.name))
        else:
            print('经过%d回合游戏，%s成功击杀%s，成为本局游戏的胜利者。' % (count,self.player1.name,self.player2.name))
a = Gameperson('八里公路',5000,1000,0.5,0.5)
b = Gameperson('大魔王',10000,500,0.2,0.2)
c = Chuanqi()
c.playGame()