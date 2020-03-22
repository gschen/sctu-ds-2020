import random
class Person():
    def __init__(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crit=crit
        self.avoid=avoid
    # 攻击
    def attack(self,object):
        # 对方是否闪避本次攻击
        if random.random() >= object.avoid:
            # 是否造成暴击
            if random.random() <=self.crit:
                print("造成双倍伤害")
                object.blood-=self.power*2
            else:
                object.blood-=self.power
        else:
            print("----miss")
class Game():
    def __init__(self,one,two):
        self.one=one
        self.two=two
    def solo(self):
        while True:
            self.one.attack(self.two)
            if self.two.blood<=0:
                print("{}活到了最后".format(self.one.name))
            self.two.attack(self.one)
            if self.one.blood<=0:
                print("{}活到了最后".format(self.two.name))
                break
lg=Person("老官",470,47,0.3,0.2)
jj=Person("江江",500,50,0.4,0.2)
sl=Game(lg,jj)
sl.solo()


