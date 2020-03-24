import random
class Person():
    def __init__(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crit=crit
        self.avoid=avoid
    #攻击
    def attack (self.object):
        print(self.name,'开始攻击')
        if random.random()>=object.avoid:
            if random.random()<=self.crit:
                object.blood=-self.power*2
                print('造成双倍伤害')
            else:
                print('......造成{}')
                object.blood=-self.power
        else:
            print('.....miss')
class Game():
    def __init__(self,one,two):
        self.one=one
        self.two=two
    def solo(self):
        while True:
            self.one.attack(self.two)
            if self.two.blood<=0:
                print()