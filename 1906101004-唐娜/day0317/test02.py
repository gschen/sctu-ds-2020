import random
class Person():
    def __init__(self,name,blood,power,crid,avoid):
        self.name=name
        self.blood=blood
        self.power=power
        self.crid=crid
        self.avoid=avoid
        #攻击
    def attack(self,object):
        print(self.name,"开始攻击")
        #对方是否闪避本次攻击
        #表示我方命中
        if random.random() >= object.avoid:
            #判断是否暴击
            if random.random() <= self.crid:
                print("-------造成双倍伤害")
                object.blood-=self.power*2
            else:
                object.blood-=self.power
            else:
                print("-------miss")
class Game():
    def __init__(self,one,two):
        #导入solo双方
        self.one=one
        self.two=two    
    def solo(self):
        while True:
            self.one.attack(two)      
            if two.blook<=0:    
                print("{}活到了最后".format(self.one.name))
                break     
            self.two.attack(one)    
            if oneblook<=0:     
                print("{}活到了最后".format(self.two.name))
                break
lg=Person()    
jj=Person()
sl=Game(lg,jj)     
sl.solo()