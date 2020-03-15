import random
class Rone():
    def __init__(self,name,blood,attack):
        self.name = name
        self.blood = blood
        self.attack =attack
    def attack_rtwo(self,rtwo):
        rand_num = random.randint(0,1)
        if rand_num <= 0.2:
            self.attack2_rtwo(rtwo)
        else:
            self.attack1_rtwo(rtwo)
    def attack1_rtwo(self,rtwo):
        rtwo.blood -= self.attack
        print("%s 攻击 %s：%s剩余生命值:%d" % (self.name, rtwo.name,rtwo.name,rtwo.blood))
    def attack2_rtwo(self,rtwo):
        rtwo.blood -= (self.attack )*2
        print("%s 暴击 %s：%s剩余生命值:%d"% (self.name, rtwo.name,rtwo.name,rtwo.blood))
    def attack3_rtwo(self):
        rtwo.blood = rtwo.blood
        print("%s 攻击 %s：%s剩余生命值:%d"% (self.name, rtwo.name,rtwo.name,rtwo.blood))
class Rtwo():
    def __init__(self, name, blood, attack):
        self.name = name
        self.blood = blood
        self.attack = attack
    def attack_rone(self, rone):
        rone.blood -= self.attack
        print("%s 攻击%s：%s剩余生命值:%d"
              % (self.name, rone.name,rone.name,rone.blood))
count = 1
role_one = Rone('KK',100,20)
role_two = Rtwo('JJ',160,30)
while True:
    print("第%d回合"%count)
    if role_one.blood > 0:
        role_one.attack_rtwo(role_two)
        if role_two.blood <= 0:
            print("KK获胜")
            break
    if role_two.blood > 0:
        role_two.attack_rone(role_one)
        if role_one.blood <= 0:
            print("JJ获胜")
            break
    count += 1
