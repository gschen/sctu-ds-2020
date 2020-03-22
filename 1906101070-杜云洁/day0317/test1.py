import random
class Person():
    def __init__(self,name,blood,power,crit,avoid):
        self.name=name
        self.blood=blood
        self.powepower
        self.crit=crit
        self.avoid=avoid
     #攻击   
    def attack(self,object):
        print(self.name,'开始攻击')
        
        #对方是否闪避攻击
        #表示我方命中
        if random.random Object.avoid:
            #判断是否暴击
            if random.random() <=self.crit:
                object.blood-=self.power*2
            else:
                object.blood-=self.power
        else:
            print('------miss')
            
class Game():
    def __init__(self,one,two):
        #导入solo双方  
        self.one=one
        self.two=two
    def solo(self):
        while True:
            self.one.attack(two)
            if two.blood<=0:
                print('{}活到了最后'.format(one))
                break
            self.two.attack(one)
            if one.blood<=0:
                print('{}活到了最后'.format(two))
                break
lg=Person('小明',500,500,0.3,0.4)
jj=Person('小江',500,40,0.2,0.3)            
s1=Game(lg,jj)
sl.solo()           