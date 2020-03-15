import random

class GamePlayer():
	def __init__(self,name,blood,attack,violence,dodge):
		self.name=name
		self.blood=blood
		self.attack=attack
		self.violence=violence
		self.dodge=dodge
	def information(self):
		print('玩家名称:%s；血量:%s；攻击力:%s；暴击率:%s；闪避率:%s' % (self.name,self.blood,self.attack,self.violence,self.dodge))
a=GamePlayer('小明',2000,100,0.4,0.1)
b=GamePlayer('小红',2000,100,0.1,0.4)
a.information()
b.information()



class Fight():
    def __init__(self):
        self.a = a
        self.b = b


    def playgame(self):
        print('游戏开始')
        n = 1
        while self.a.blood > 0 and self.b.blood > 0:
            print('第{}回合开始'.format(n))
            a = 1
            b = 1
            while a == 1:
                if random.random() <= self.b.dodge:
                    print('{}的攻击被{}闪避'.format(self.a.name, self.b.name))

                elif random.random() <= self.a.violence:
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.a.name,self.a.attack*2))
                    self.b.blood -= self.a.attack*2
                else:
                    print('{}进行了攻击，造成了{}点伤害'.format(self.a.name,self.a.attack))
                    self.b.blood -= self.a.attack
                a = 0
            while b == 1:
                if random.random() <= self.a.dodge:
                    print('{}的攻击被{}闪避'.format(self.b.name, self.a.name))

                elif random.random() <= self.b.violence:
                    print('{}的攻击暴击了，造成了{}点伤害'.format(self.b.name,self.b.attack*2))
                    self.a.blood -= self.b.attack*2
                else:
                    print('{}进行了攻击，造成了{}点伤害'.format(self.b.name,self.b.attack))
                    self.a.blood-= self.b.attack
                b = 0
            print('第{}回合结束，{}剩余{}点生命值，{}剩余{}点生命值'.format(n,self.a.name,self.a.blood,self.b.name,self.b.blood))
            n += 1
        if  self.a.blood < 0 and self.b.blood > 0:
            print('因此，{}获得胜利'.format(self.b.name))
        elif  self.a.blood > 0 and self.b.blood < 0:
            print('因此，{}获得胜利'.format(self.a.name))
        else:
            print('双方同时倒下')

a=GamePlayer('小明',2000,100,0.4,0.1)
b=GamePlayer('小红',2000,100,0.1,0.4)
c= Fight()
c.playgame()