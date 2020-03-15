import random
class role():
    def init(self, name, hp, damage,cs,ea):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.cs = cs
        self.ea = ea

class Game():
    def __init__(self,number):
        self.number=number
        self.a=Person()
        self.b=Person()

def playGame(self):
    count = 1
    while self.a.hp > 0 and self.b.hp > 0:
        c = input('输入：')
        a = 1
        b = 1
        if random.random() <= self.b.ea:
            print('{}攻击，{}闪避'.format(self.a.name, self.b.name))
        elif random.random() <= self.a.cs:
            print('{}暴击，造成{}攻击力'.format(self.a.name,self.a.damage*2))
            self.b.hp -= self.a.damage*2
        else:
            print('{}攻击，造成{}攻击力'.format(self.a.name,self.a.damage))
            self.b.hp -= self.a.damage
        if random.random() <= self.a.ea:
            print('{}攻击，{}闪避'.format(self.b.name, self.a.name))
        elif random.random() <= self.b.cs:
            print('{}暴击，造成{}攻击力'.format(self.b.name,self.b.damage*2))
            self.a.ph -= self.b.damage*2
        else:
            print('{}攻击，造成{}攻击力'.format(self.b.name,self.b.damage))
            self.a.ph-= self.b.damage
            print('{}剩余{}血量，{}剩余{}血量'.format(self.a.name,self.a.ph,self.b.name,self.b.ph))
            count += 1
        if  self.a.ph < 0 and self.b.ph > 0:
            print('最后，{}胜利'.format(self.b.name))
        elif  self.a.ph > 0 and self.b.ph < 0:
            print('最后，{}胜利'.format(self.a.name))
        else:
            print('双方都失败')