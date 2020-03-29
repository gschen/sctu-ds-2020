# 回合制人物Pk游戏
# 创建一个角色类(类)，包含属性有：角色名称、角色血量、攻击力、暴击率、闪避率。
# 创建一个游戏类，属性包含参加游戏的双方（对象），方法有playGame，参加游戏的双方互相攻击，可能产生暴击-----攻击力*2，可能闪避----闪避当前对方的攻击，直到一方血量<0，游戏结束。该方法打印每一轮游戏的情况，以及最终的获胜情况。

# 备注：如果暴击率是0.2可以用以下语句判断是否造成暴击
# if random.random() <= 0.2:
# 	pass

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
        #对方是否闪避本次攻击
        #表示我方命中
        if random.random() >=object.avoid:
            #判断是否暴击
            if random.random() <=self.crit:
                print('------造成双倍伤害')
                object.blood-=self.power*2
            else:
                print('------造成{}伤害'.format(self.power))
                object.blood-=self.power
        else:
            print('-------miss')

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
                break

mm=Person('莓莓',470,47,0.3,0.2)
xm=Person('虾米',550,40,0.2,0.3)
sl=Game(mm,xm)
sl.solo()