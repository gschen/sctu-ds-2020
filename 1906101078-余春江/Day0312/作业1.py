import random
class Person():
    def __init__(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crit=crit
        self.avoid=avoid
    #攻击
    def attack(self,object):
        #对方是否闪避本次攻击
        #表示我方命中
        if random.random() >= object.avoid:
            print('未命中')
            #判断是否暴击
            if random.random() <=self.crit:
                print('会心一击，双倍伤害')
                object.blood-self.power*2
            else:
                print("未暴击")
                object.blood-self.power

class Game():
    def __init__(self,A,B):
        #导入solo双方
        self.A=A
        self.B=B
    def solo(self):
        while True:
            self.A.attack(self.B)
            if self.B.blood <= 0:
                print("{}活到了最后".format(self.A.name))
                break
            self.B.attack(self.A)
            if self.A.blood <= 0:
                print('{}活到了最后'.format(self.B.name))
                break


mr=Person("鸣人",500,50,0.3,0.1)
zz=Person("佐助",500,45,0.4,0.1)
sl=Game(mr,zz)
sl.solo()