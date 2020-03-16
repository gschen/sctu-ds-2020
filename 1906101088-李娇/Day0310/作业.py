import random
class Character:

    def __init__(self,name,HP,ATK,CRI,DOD):
        self.name = name
        self.HP = HP
        self.ATK = ATK
        self.CRI = CRI
        self.DOD = DOD

class Fight:

    def __init__(self,player_a,player_b):
        self.a = player_a
        self.b = player_b


    def playgame(self):
        print('游戏开始')
        n = 1
        while self.a.HP > 0 and self.b.HP > 0:
            c = input('输入任意内容即可开始一次相互伤害：')
            print('第{}回合开始'.format(n))
            a = 1
            b = 1
            while a == 1:
                if random.random() <= self.b.DOD:
                    print('{}的攻击被{}闪避'.format(self.a.name, self.b.name))

                elif random.random() <= self.a.CRI:
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.a.name,self.a.ATK*2))
                    self.b.HP -= self.a.ATK*2
                else:
                    print('{}进行了攻击，造成了{}点伤害'.format(self.a.name,self.a.ATK))
                    self.b.HP -= self.a.ATK
                a = 0
            while b == 1:
                if random.random() <= self.a.DOD:
                    print('{}的攻击被{}闪避'.format(self.b.name, self.a.name))

                elif random.random() <= self.b.CRI:
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.b.name,self.b.ATK*2))
                    self.a.HP -= self.b.ATK*2
                else:
                    print('{}进行了攻击，造成了{}点伤害'.format(self.b.name,self.b.ATK))
                    self.a.HP-= self.b.ATK
                b = 0
            print('第{}回合结束，{}剩余{}点生命值，{}剩余{}点生命值'.format(n,self.a.name,self.a.HP,self.b.name,self.b.HP))
            n += 1
        if  self.a.HP < 0 and self.b.HP > 0:
            print('因此，{}获得胜利'.format(self.b.name))
        elif  self.a.HP > 0 and self.b.HP < 0:
            print('因此，{}获得胜利'.format(self.a.name))
        else:
            print('双方同时倒下')
one=Fight("A","B")
one.playgame()