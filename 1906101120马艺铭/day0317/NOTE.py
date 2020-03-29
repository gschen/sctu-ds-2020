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
        if random.random object.avoid：
            #判断是否暴击
            if random.random() <=self.crit:
                print('造成双倍伤害')
                object.blood-=self.power
            else:
                object.blood-=self .power
        else:
            print('miss')
        

    class Game():
        def __init__(self,one,two):
            #导入solo双方
            self.one=one
            self.two=two
        def solo(self):
            while Ture:
                self.one.attcak(self.two)
                if two.blood<=0:
                    print('{}活到了最后'.format(self.one.name))
                    break
                self.two.attck(self.one)
                if two.blood<=0:
                    print('{}活到了最后'.format(self.two.name))
                    break


