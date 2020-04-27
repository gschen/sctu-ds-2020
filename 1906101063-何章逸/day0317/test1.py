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
        print(self.name,'开始攻击')
        #对方是否闪避
        #表示我方命中
        if random.random() >=object.avoid:
#判断是否暴击
            if random.random() <= self.crit:
                print('2倍攻击')
                object.blood-=self.power*2
            else:
                print('-----造成{}'.format(self.power))
                object.blood-=self.power
        else:
            print('....miss')

class Game():
    def __init__(self,one,two):
        #导入solo双方
        self.one=one
        self.two=two

    def solo(self):
        while True:
            self.one.attack(self.two)
            if self.two.blood<=0:
                print('{}活到了最后'.format(self.one.name))
                break
            self.two.attack(self.one)
            if self.one.blood<=0:
                print('{}活到了最后'.format(self.two.name))

jia=Person('jia',470,47,0.3,0.2)
zhen=Person('zhen',550,40,0.2,0.3)
s1=Game(jia,zhen)
s1.solo()

    