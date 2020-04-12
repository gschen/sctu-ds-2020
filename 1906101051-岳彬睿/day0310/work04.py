import random
class player:
    def __init__(self,name,HP,ATK,CRI):
        self.ID = ID
        self.HP = HP
        self.ATK = ATK
        self.CRI = CRI

class Fight:
    def __init__(self,player_a,player_b):
        self.a = player_a
        self.b = player_b

    def playgame(self):
        print('Game Start')
        n = 1
        while self.a.HP > 0 and self.b.HP > 0:
            c = input('请选择一个武器进行攻击：')
            print('第{}回合开始'.format(n))
            a = 1
            b = 1
            while a == 1:
                if random.random() <= self.a.CRI:
                    print('{}打出暴击，造成{}点伤害'.format(self.a.name,self.a.ATK*2))
                    self.b.HP -= self.a.ATK*2
                elif:
                    print('{}进行攻击，造成{}点伤害'.format(self.a.name,self.a.ATK))
                    self.b.HP -= self.a.ATK
                a = 0
            while b == 1:
                if random.random() <= self.b.CRI:
                    print('{}打出暴击，造成{}点伤害'.format(self.b.name,self.b.ATK*2))
                    self.a.HP -= self.b.ATK*2
                elif:
                    print('{}进行攻击，造成了{}点伤害'.format(self.b.name,self.b.ATK))
                    self.a.HP-= self.b.ATK
                b = 0
            print('第{}回合结束，{}剩余{}点生命值，{}剩余{}点生命值'.format(n,self.a.name,self.a.HP,self.b.name,self.b.HP))1
            n += 1
        if self.a.HP < 0 and self.b.HP > 0:
            print('{}获得胜利'.format(self.b.name))
        elif  self.a.HP > 0 and self.b.HP < 0:
            print('{}获得胜利'.format(self.a.name))
        else:
            print('平局')
